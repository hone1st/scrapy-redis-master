import random
import logging
from scrapy.exceptions import IgnoreRequest

# 导入redis的connect开门钥匙
from master1886.settings import AGENT_POOL
from master1886.util.redisutil import UtilRedis

# 导入TRYTIME和AGENTPOOL在setting.py中


class SlaveAgentMiddleware(object):

    # process_request(self, request, spider)

    def process_request(self, request, spider):
        # 随机设置请求头
        request.headers["User-Agent"] = random.choice(AGENT_POOL)

