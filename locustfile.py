import os
import redis
import time
import datetime
from locust import User, task, events
import random
import string

class RedisClient(object):
    def __init__(self):
        
        # set up of connection details
        redis_url = os.getenv('REDIS_URL', 'localhost')
        redis_port = os.getenv('REDIS_PORT', '6379')
        username = os.getenv('REDIS_USERNAME', 'username')
        password = os.getenv('REDIS_PASSWORD', 'changeme')

        self.rc = redis.Redis(host=redis_url, port=redis_port, db=0, decode_responses=True)

    def get_redis(self, key, command='GET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.get(key)
            # print (result)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key+"  -  "+result, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key+"  -  "+result, response_time=total_time, response_length=length)

    def set_redis(self, key, value, command='SET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.set(key, value)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def hset_redis(self, hashkey, key, value, command='HSET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.hset(hashkey, key, value)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key, response_time=total_time,
                                        response_length=length)
        return result

    def hget_redis(self, hashkey, key, command='HGET'):
        result = None
        start_time = time.time()
        try:
            result = self.rc.hget(hashkey, key)
            # print (result)
            if not result:
                result = ''
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=command, name=key+"  -  "+result, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            length = len(str(result))
            events.request_success.fire(request_type=command, name=key+"  -  "+result, response_time=total_time, response_length=length)


class RedisUser(User):
    def __init__(self, *args, **kwargs):
        super(RedisUser, self).__init__(*args, **kwargs)
        self.client = RedisClient()


        # Rendom word generation
        length1 = random.randrange(1,20)
        length2 = random.randrange(1,20)
        self.result_str1 = ''.join(random.choice(string.ascii_letters) for i in range(length1))
        self.result_str2 = ''.join(random.choice(string.ascii_letters) for i in range(length2))


    @task(1)
    def test1 (self):
        for i in range (1,10):
            self.client.set_redis(self.result_str1,self.result_str2)

        for i in range(1,1000):
            self.client.get_redis(self.result_str1)

    
    @task(2)
    def test3 (self):
        for i in range (1,1000):
            self.client.set_redis(self.result_str1,self.result_str2)

        for i in range(1,10):
            self.client.get_redis(self.result_str1)

    @task(3)
    def test4 (self):
        for i in range (1,1000):
            self.client.set_redis(self.result_str1,self.result_str2)

        for i in range(1,10):
            self.client.hget_redis("RandomWords",self.result_str1)

    @task(4)
    def test2 (self):
        for i in range (1,10):
            self.client.hset_redis("RandomWords",self.result_str1,self.result_str2)

        for i in range(1,1000):
            self.client.get_redis(self.result_str1)


            
    # @task
    # def set(self):
    #     for i in range (1,10):
    #         self.client.get_redis(self.result_str1)

    # @task
    # def get(self):
    #     for i in range (1,1000):
    #         self.client.set_redis(self.result_str1, self.result_str2)

    # @task
    # def hset(self):
    #     self.client.hset_redis("RandomWords","Hello", "World")
    
    # @task
    # def hget(self):
    #     self.client.hget_redis("RandomWords","Hello")