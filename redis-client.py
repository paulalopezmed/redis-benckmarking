import os
import redis

# set up of connection details
redis_url = os.getenv('REDIS_URL', 'localhost')
redis_port = os.getenv('REDIS_PORT', '6379')
username = os.getenv('REDIS_USERNAME', 'username')
password = os.getenv('REDIS_PASSWORD', 'changeme')

# stablish connection with Redis server
r = redis.Redis(host=redis_url, port=redis_port, db=0, decode_responses=True)

r.set('foo', 'bar')
result = r.get('foo')

print(result)