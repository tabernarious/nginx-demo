from flask import Flask
from redis import Redis
import time
from datetime import datetime
from datetime import timezone

app = Flask(__name__)
cache = Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('app1_hits')
        except cache.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')

def hello():
  count = get_hit_count()
  dateTimeUTC = datetime.now(tz=timezone.utc)
  return 'Hello! This is App1 :)<br><br>Viewed {} times!<br><br>{} UTC'.format(count, dateTimeUTC)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
