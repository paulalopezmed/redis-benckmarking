import os
import redis
import random
import string

# set up of connection details
redis_url = os.getenv('REDIS_URL', 'localhost')
redis_port = os.getenv('REDIS_PORT', '6379')
username = os.getenv('REDIS_USERNAME', 'username')
password = os.getenv('REDIS_PASSWORD', 'changeme')

# stablish connection with Redis server
r = redis.Redis(host=redis_url, port=redis_port, db=0, decode_responses=True)

#esto es lo modificado el 28/01/22
# Call a large amount of time with GET and HGET to a entry that has been stablish with SET and to another ones stablish by HSET

for i in range (1,10):
    result_num = random.randrange(100)
    length = random.randrange(1,20)
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # r.hset("NumberVsString", str(result_num), result_str)
    r.set(result_num, result_str)
    # result= r.hget("NumberVsString", str(result_num))
    # print(result)
    # print(result_num)
    # print (result_str)

for i in range (1,100000):
    #result= r.get("NumberVsString", str(result_num))
    r.get(result_num)
    #print(result)
# Call some times and entry that is stablish a large amount of times with SET and HSET

#r.hset("foo", "bar", "2")
#r.hset("NumberVsString", "3", "Three")
#result = r.hget("foo", "bar")
#result= r.hget("NumberVsString", "3")

print(result)