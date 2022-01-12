#!/usr/local/bin/python3

# Copyright (c) 2020 Stanford University
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR(S) DISCLAIM ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL AUTHORS BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
This file computes key metrics from Paxos client logfiles. The logfile format is
specified in src/client/client.go.
"""

import json
import numpy as np
from os import path
import statistics

def get_metrics(dirname):
    """
    Computes key metrics about an experiment from the client-side logfiles, and
    returns them as a dictionary. 'dirname' specifies the directory in which the
    client-side logfiles are stored.
    """
    with open(path.join(dirname, 'lattput.txt')) as f:
        tputs = []
        for l in f:
            l = l.split(' ')
            tputs.append(float(l[2]))

    with open(path.join(dirname, 'latFileRead-0.txt')) as f:
        exec_lats_read0 = []
        # commit_lats = []
        for l in f:
            l = l.split(' ')
            exec_lats_read0.append(float(l[1]))
            # commit_lats.append(float(l[2]))

    with open(path.join(dirname, 'latFileRead-1.txt')) as f:
        exec_lats_read1 = []
        for l in f:
            l = l.split(' ')
            exec_lats_read1.append(float(l[1]))

    with open(path.join(dirname, 'latFileRead-2.txt')) as f:
        exec_lats_read2 = []
        for l in f:
            l = l.split(' ')
            exec_lats_read2.append(float(l[1]))

    with open(path.join(dirname, 'latFileRead-3.txt')) as f:
        exec_lats_read3 = []
        for l in f:
            l = l.split(' ')
            exec_lats_read3.append(float(l[1]))

    with open(path.join(dirname, 'latFileRead-4.txt')) as f:
        exec_lats_read4 = []
        for l in f:
            l = l.split(' ')
            exec_lats_read4.append(float(l[1]))

    with open(path.join(dirname, 'latFileWrite-0.txt')) as f:
        exec_lats_write0 = []
        # commit_lats = []
        for l in f:
            l = l.split(' ')
            exec_lats_write0.append(float(l[1]))
            # commit_lats.append(float(l[2]))

    with open(path.join(dirname, 'latFileWrite-1.txt')) as f:
        exec_lats_write1 = []
        for l in f:
            l = l.split(' ')
            exec_lats_write1.append(float(l[1]))

    with open(path.join(dirname, 'latFileWrite-2.txt')) as f:
        exec_lats_write2 = []
        for l in f:
            l = l.split(' ')
            exec_lats_write2.append(float(l[1]))

    with open(path.join(dirname, 'latFileWrite-3.txt')) as f:
        exec_lats_write3 = []
        for l in f:
            l = l.split(' ')
            exec_lats_write3.append(float(l[1]))

    with open(path.join(dirname, 'latFileWrite-4.txt')) as f:
        exec_lats_write4 = []
        for l in f:
            l = l.split(' ')
            exec_lats_write4.append(float(l[1]))

    return {
        #'mean_lat_commit': statistics.mean(commit_lats),
        #'p50_lat_commit': np.percentile(commit_lats, 50),
        #'p90_lat_commit': np.percentile(commit_lats, 90),
        #'p95_lat_commit': np.percentile(commit_lats, 95),
        #'p99_lat_commit': np.percentile(commit_lats, 99),
        'mean_Read0': statistics.mean(exec_lats_read0),
        'p50_Read0': np.percentile(exec_lats_read0, 50),
        'p90_Read0': np.percentile(exec_lats_read0, 90),
        'p95_Read0': np.percentile(exec_lats_read0, 95),
        'p99_Read0': np.percentile(exec_lats_read0, 99),
        'p999_Read0': np.percentile(exec_lats_read0, 99.9),
        'p9999_Read0': np.percentile(exec_lats_read0, 99.99),
        'mean_Read1': statistics.mean(exec_lats_read1),
        'p50_Read1': np.percentile(exec_lats_read1, 50),
        'p90_Read1': np.percentile(exec_lats_read1, 90),
        'p95_Read1': np.percentile(exec_lats_read1, 95),
        'p99_Read1': np.percentile(exec_lats_read1, 99),
        'p999_Read1': np.percentile(exec_lats_read1, 99.9),
        'p9999_Read1': np.percentile(exec_lats_read1, 99.99),
        'mean_Read2': statistics.mean(exec_lats_read2),
        'p50_Read2': np.percentile(exec_lats_read2, 50),
        'p90_Read2': np.percentile(exec_lats_read2, 90),
        'p95_Read2': np.percentile(exec_lats_read2, 95),
        'p99_Read2': np.percentile(exec_lats_read2, 99),
        'p999_Read2': np.percentile(exec_lats_read2, 99.9),
        'p9999_Read2': np.percentile(exec_lats_read2, 99.99),
        'mean_Read3': statistics.mean(exec_lats_read3),
        'p50_Read3': np.percentile(exec_lats_read3, 50),
        'p90_Read3': np.percentile(exec_lats_read3, 90),
        'p95_Read3': np.percentile(exec_lats_read3, 95),
        'p99_Read3': np.percentile(exec_lats_read3, 99),
        'p999_Read3': np.percentile(exec_lats_read3, 99.9),
        'p9999_Read3': np.percentile(exec_lats_read3, 99.99),
        'mean_Read4': statistics.mean(exec_lats_read4),
        'p50_Read4': np.percentile(exec_lats_read4, 50),
        'p90_Read4': np.percentile(exec_lats_read4, 90),
        'p95_Read4': np.percentile(exec_lats_read4, 95),
        'p99_Read4': np.percentile(exec_lats_read4, 99),
        'p999_Read4': np.percentile(exec_lats_read4, 99.9),
        'p9999_Read4': np.percentile(exec_lats_read4, 99.99),
        'mean_Write0': statistics.mean(exec_lats_write0),
        'p50_Write0': np.percentile(exec_lats_write0, 50),
        'p90_Write0': np.percentile(exec_lats_write0, 90),
        'p95_Write0': np.percentile(exec_lats_write0, 95),
        'p99_Write0': np.percentile(exec_lats_write0, 99),
        'p999_Write0': np.percentile(exec_lats_write0, 99.9),
        'p9999_Write0': np.percentile(exec_lats_write0, 99.99),
        'mean_Write1': statistics.mean(exec_lats_write1),
        'p50_Write1': np.percentile(exec_lats_write1, 50),
        'p90_Write1': np.percentile(exec_lats_write1, 90),
        'p95_Write1': np.percentile(exec_lats_write1, 95),
        'p99_Write1': np.percentile(exec_lats_write1, 99),
        'p999_Write1': np.percentile(exec_lats_write1, 99.9),
        'p9999_Write1': np.percentile(exec_lats_write1, 99.99),
        'mean_Write2': statistics.mean(exec_lats_write2),
        'p50_Write2': np.percentile(exec_lats_write2, 50),
        'p90_Write2': np.percentile(exec_lats_write2, 90),
        'p95_Write2': np.percentile(exec_lats_write2, 95),
        'p99_Write2': np.percentile(exec_lats_write2, 99),
        'p999_Write2': np.percentile(exec_lats_write2, 99.9),
        'p9999_Write2': np.percentile(exec_lats_write2, 99.99),
        'mean_Write3': statistics.mean(exec_lats_write3),
        'p50_Write3': np.percentile(exec_lats_write3, 50),
        'p90_Write3': np.percentile(exec_lats_write3, 90),
        'p95_Write3': np.percentile(exec_lats_write3, 95),
        'p99_Write3': np.percentile(exec_lats_write3, 99),
        'p999_Write3': np.percentile(exec_lats_write3, 99.9),
        'p9999_Write3': np.percentile(exec_lats_write3, 99.99),
        'mean_Write4': statistics.mean(exec_lats_write4),
        'p50_Write4': np.percentile(exec_lats_write4, 50),
        'p90_Write4': np.percentile(exec_lats_write4, 90),
        'p95_Write4': np.percentile(exec_lats_write4, 95),
        'p99_Write4': np.percentile(exec_lats_write4, 99),
        'p999_Write4': np.percentile(exec_lats_write4, 99.9),
        'p9999_Write4': np.percentile(exec_lats_write4, 99.99),
        'avg_tput': statistics.mean(tputs),
        # 'total_ops': len(tputs),
    }

if __name__ == '__main__':
    """
    Computes client metrics from the root epaxos directory, which is where the
    files are stored on the remote client machines. Logs the metrics to stdout
    in json format.
    """
    #print(json.dumps(get_metrics(path.expanduser('/Users/tsengle/GolandProjects/gus-epaxos/'))))
    print(json.dumps(get_metrics(path.expanduser('/root/go/src/gus-epaxos/'))))