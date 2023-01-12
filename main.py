import subprocess
import sys
import time

import concurrent.futures

run_id = sys.stdin.readline()


def collector():
    time.sleep(15)
    save_logs(1)


def save_logs(t):
    print('saving logs for iteration ', t)
    k = ['bridges', 'lights', 'lights-nodas']
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # range here is how much pods per group we have
        for i in k:
            if i == 'lights-nodas':
                for j in range(20):
                    executor.submit(record_log, i, j)
            else:
                for j in range(100):
                    executor.submit(record_log, i, j)


def record_log(i, k):
    f = open(str(k) + '-' + str(i) + '.log', 'w')
    c = 'tg-celestia-' + str(run_id.split('\n')[0]) + '-' + str(i) + '-' + str(k) + ''
    subprocess.call(
        ['kubectl', 'logs', c],
        stdout=f)


collector()
