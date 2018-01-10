#  REDIS_URL = 'redis://localhost:6379/4'

# You can also specify the Redis DB to use
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 4
REDIS_PASSWORD = ''

# Queues to listen on, 顺序决定了rq从队列中获取数据的前后
# *将阻塞时间长, 调用频次低的队列放到前面;
# *将阻塞时间段, 调用批次搞的队列放到后面;
QUEUES = ['bamboo', 'defaults']
