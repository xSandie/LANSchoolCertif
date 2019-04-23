import redis
cookie_redis = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)#cookie存到1号数据库
