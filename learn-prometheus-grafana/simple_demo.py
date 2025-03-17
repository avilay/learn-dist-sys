"""
Start Prometheus:
$ /usr/local/prometheus/prometheus --config.file=prometheus.yml

Prometheus will be started http://localhost:9090

Start grafna:
$ /usr/local/grafana/bin/grafana-server -homepath /usr/local/grafana web

Grafana will be started on http://localhost:3000

In the grafana dashboard add a new dashboard, choose the datasource as prometheus. All the metrics will be automatically
available here.
"""

from prometheus_client import start_http_server, Summary, Gauge, Histogram, Info
import random
import time
from datetime import datetime
from haikunator import Haikunator
import numpy as np

# Summary definition will result in two metrics - request_processing_seconds_sum and request_processing_seconds_count
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


# Can also just directly use REQUEST_TIME.observe(val)
@REQUEST_TIME.time()
def learn_gauge(run_id):
    loss_fn = Gauge('loss_function_values', 'Value of loss function', ['run_id', 'samples'])
    info = Info('demo_metadata', 'Some static metadata of this demo')
    info.info({'version': '1.2.3', 'buildhost': 'foo@bar', 'run_id': run_id})
    cont = True
    while cont:
        for i in range(50):
            # Train
            time.sleep(random.random())
            train_loss = random.random()
            # print(f'{datetime.now()}Training loss: {train_loss}')
            loss_fn.labels(run_id=run_id, samples='train').set(train_loss)

            # Validate
            time.sleep(random.random())
            val_loss = random.random()
            # print(f'{datetime.now()} Validation loss: {val_loss}')
            loss_fn.labels(run_id=run_id, samples='val').set(val_loss)
        cont = input('Another run (y/n)? ') == 'y'


def learn_hist(run_id, iters=1000):
    """
    This will result in three metrics - my_random_sample_buckets, my_random_sample_sum, and my_random_sample_counts.
    The last two are pretty much useless. my_random_sample_buckets tells me how many elements in each bucket do I have.
    Grafana does not do a very good job of graphing this. It just shows up as a standard line graph.
    """
    h = Histogram('my_random_sample', 'Description of my random sample', ['run_id'])
    cont = True
    while cont:
        for _ in range(iters):
            h.labels(run_id=run_id).observe(np.random.standard_normal())
            time.sleep(random.random())
        cont = input('Another run (y/n)? ') == 'y'
        
        
def learn_summary(run_id, iters=50):
    """
    This will result in three metrics -
      - my_simple_summary_created: This is a timestamp of when the summary was created
      - my_simple_summary_count: This the number of times this metric was emitted
      - my_simple_summary_sum: This is the sum of all the value emitted so far
    """
    s = Summary('my_simple_summary', 'Summary description here')
    cont = True
    while cont:
        for _ in range(iters):
            s.observe(np.random.standard_normal())
            time.sleep(random.random())
        cont = input('Another run (y/n)? ') == 'y'


if __name__ == '__main__':
    start_http_server(8000)
    run_id = Haikunator().haikunate()
    print(f'Starting {run_id}')
    # learn_gauge(run_id)
    learn_hist(run_id)
    # learn_summary(run_id)

