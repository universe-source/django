"""
rq 使用实例
    1 启动rq 工作进程(worker): 其中仅仅包含2个队列bamboo, 'defaults';
        一个worker就是一个后台运行的Python进程;

    2 每一个task都用 Job 类实例来表示, 保存id, 所属队列, 函数, 执行结果等信息, 
        实例信息保存在redis的hash结构中, <uid>采用uuid.uuid4生成.

    3 每一个队列都用 Queue 类实例来表示, 负责保存和处理任务, 存储job的id值,
        队列信息保存在redis的list结构中, rq:queue:<name>

worker生命周期:
    1 启动, 载入python环境, 将worker注册到系统环境中;
    2 开启监听, 对指定的db/port, 多个queue name进行监听, 应该使用(UNIX Socket)来实现的吧
    3 遍历Queues, 弹出非空queue中的job--job1
        fork子进程处理job1任务(见perform_job);
        父进程等待子进程处理结束或者超时;
        根据返回结构设置redis中的key值;
    4 继续下一个队列处理

worker状态:
    Started: 开启完成
    suspended: 暂停中
    busy: 忙中
    idle: 闲置中

Job状态:
    queued: 在准备队列中
    finished: 已经完成
    failed: 失败
    started: 运行中, 在prepare_job_execution中被置
    deferred: 延迟的

burst:
    遍历workers中的所有queues, 一旦处理完成, 即queues为空的时候, 立刻退出

输出:
    DEBUG: 有详细的信息输出

redis key:
    Queues:
        rq:queues(set): 当前正在运行中的queue, 对于快速执行完的task, 这里一般为空
        rq:queue:failed: 当且仅当子进程没有正常返回(不是finished/failed)时才会存储
                    见rq/worker.py(_monitor_work_horse_tick)
        rq:job:task-id: 其中task-id在入队就生成, 但是redis键值在server端执行的时候
                    才会生成, 会设置超时时间, 见rq/worker.py(prepare_job_execution)

结束处理
    一个worker在接收到 SIGINT/SIGTERM 时, 等待current running task完成, 之后平滑自杀;
    在停止期间再次收到 SIGINT/SIGTERM 时, 强制杀死task(SIGKILL), 之后自杀;
    ----表现处理的现象就是, rq worker有时候需要按两次 CTRL + C;
"""
import time
from redis import Redis, StrictRedis
from rq import Queue
import cb


#  q = Queue('bamboo', connection=StrictRedis(db=4), default_timeout=600)
q = Queue('bamboo', connection=StrictRedis(db=4))
# 其中
#   key == rq:queue:bamboo
#   redis_queues_keys == rq:queues
#   redis_queue_namespace_prefix == rq:queue:
#   task的键值: rq:job:a6511508-f748-4d55-8dca-d0c1506cdb90
# 参数:
#   timeout: 执行任务的时间, 如果超时, 表示task[lost]
#   result_ttl: 每一个task执行完毕的返回值保存在redis的时间
#           None--永久保存
#           非None--过期时间
#       其中结果存储在key.result中, 默认永久存在
#   ttl: task的ttl时间, 默认为500, 在server出队列的时候获取(redis层面,并非python)
job = q.enqueue(cb.count_words_at_url, 'http://nvie.com')
print('Client:'
      '\n\tkey:', job.key,
      '\n\tresult(这时候可能job没有开始进行):', job.result,
      '\n\tttl:', job.ttl)

# Now, wait a while, until the worker is finished
time.sleep(2)
print('Client(等待两秒之后):'
      '\n\tkey:', job.key,
      '\n\tresult:', job.result,
      '\n\tttl:', job.ttl)
