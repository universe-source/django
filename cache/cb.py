"""
RQ Callback Function
Reference: <http://python-rq.org/docs/jobs/>
"""
import socket
import requests
from rq import get_current_job


def count_words_at_url(url):
    """
    回调函数
    """
    # 1 利用get_current_job来访问当前的task对象
    job = get_current_job()
    print(__file__, '回调函数中',
          '\n\tCurrent Job:', job,
          '\n\tkey:', job.key,
          '\n\tresult:', job.result,
          '\n\tttl:', job.ttl)

    # 2 存储自定义信息到task中, 以便之后出队之后可以使用
    job.meta['handled_by'] = socket.gethostname()
    job.save_meta()

    # 其他处理
    rsp = requests.get(url)
    return len(rsp.text.split())
