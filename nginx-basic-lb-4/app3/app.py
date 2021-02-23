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
            return cache.incr('app3_hits')
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
      appname = "App3",
      count = count,
      dateTimeUTC = dateTimeUTC
  )

@app.route('/favicon.ico')
def fav():
  return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route('/favicon-16x16.png')
def fav16():
  return send_from_directory(os.path.join(app.root_path, 'static'),'favicon-16x16.png')

@app.route('/favicon-32x32.png')
def fav32():
  return send_from_directory(os.path.join(app.root_path, 'static'),'favicon-32x32.png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
