# scrapy-redis-master
master
## master端配合slave端使用。
master 端仅用CrawlSpider 配合rule使用进行全站爬取。
#### 记录爬取的效果、电脑配置、请求配置、过滤配置
### 配置:
电脑：thinkpad w530
内存：16G
硬盘：ssd256g
网络：wifi 长城50M
### 效果：
master爬取数量10W/H
slave存储item数据3W5/H
### 请求配置：
#### master：   
请求头中：轮换agent
spider中：判断url是否存在completeurl:(set)中，存在pass,不存在存储到detailurl:（list）中
#### slave：
请求头：轮换agent，增加默认的其他header信息
ip代理：未设置（已写好获取有效的ip工具类）
在agent中间件中增加判断是否存在于indexExcepturls:中或者completeurl:  存在就raise掉
pipeline中间件中存储成功则将url存储到completeurl:中。
spider中增加处理数据异常，索引异常则存储url到indexExcepturls:中
##### redis/mysql/ipproxy工具类

