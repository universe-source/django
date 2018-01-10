import requests
from rq import get_current_job


def count_words_at_url(url):
    job = get_current_job()
    print(__file__, '回调函数中',
          '\n\tCurrent Job:', job,
          '\n\tkey:', job.key,
          '\n\tresult:', job.result,
          '\n\tttl:', job.ttl)
    rsp = requests.get(url)
    return len(rsp.text.split())
