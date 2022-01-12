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

    with open(path.join(dirname, 'latency.txt')) as f:
        exec_lats_read0 = []
        # commit_lats = []
        for l in f:
            l = l.split(' ')
            exec_lats_read.append(float(l[1]))
            # commit_lats.append(float(l[2]))



    return {
        #'mean_lat_commit': statistics.mean(commit_lats),
        #'p50_lat_commit': np.percentile(commit_lats, 50),
        #'p90_lat_commit': np.percentile(commit_lats, 90),
        #'p95_lat_commit': np.percentile(commit_lats, 95),
        #'p99_lat_commit': np.percentile(commit_lats, 99),
        'mean_Read': statistics.mean(exec_lats_read),
        'p50_Read': np.percentile(exec_lats_read, 50),
        'p90_Read': np.percentile(exec_lats_read, 90),
        'p95_Read': np.percentile(exec_lats_read, 95),
        'p99_Read': np.percentile(exec_lats_read, 99),
        'p999_Read': np.percentile(exec_lats_read, 99.9),
        'p9999_Read': np.percentile(exec_lats_read, 99.99),
        'mean_Write0': statistics.mean(exec_lats_write),
        'p50_Write0': np.percentile(exec_lats_write, 50),
        'p90_Write0': np.percentile(exec_lats_write, 90),
        'p95_Write0': np.percentile(exec_lats_write, 95),
        'p99_Write0': np.percentile(exec_lats_write, 99),
        'p999_Write0': np.percentile(exec_lats_write, 99.9),
        'p9999_Write0': np.percentile(exec_lats_write, 99.99),
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
