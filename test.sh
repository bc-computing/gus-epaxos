timeout 180s bin/client -maddr=10.10.1.1 -writes=$1 -c=$2 -T=$3
python3.8 n-5-client_metrics.py
