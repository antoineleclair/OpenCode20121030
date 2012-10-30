import requests
from datetime import datetime
import time

while True:
    post = dict(
        content='Hello from worker %s' % str(datetime.now())
    )
    r = requests.post('http://shout-oc.aws.af.cm/shout', data=post)
    print r.status_code
    print 'Sleeping', datetime.now()
    time.sleep(10)
