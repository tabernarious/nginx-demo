from flask import Flask, render_template, send_from_directory
from redis import Redis
import time
import os
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
  return render_template(
      'app.html',
      appname = "App1",
      count = count,
      dateTimeUTC = dateTimeUTC
  )

@app.route('/favicon.ico')

def fav():
  return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
