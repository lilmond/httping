A simple HTTP/HTTPS server pinger made in Python.

# Installation
Linux
```
git clone https://github.com/lilmond/httping/
cd httping
```

# Usage
```
python httping.py --help
```
```
usage: httping.py [-h] [-t TIMEOUT] [-nv] URL

A simple HTTP server pinger.

positional arguments:
  URL                   Target's full URL.

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Socket connection timeout value.
  -nv, --no-verify      Whether to verify SSL if the connection is HTTPS.
```

# Example
```
python httping.py https://www.roblox.com/login
```
```
[13:28:47 10-02-2024][INFO] Initializing HTTP Pinger on www.roblox.com:443...
[13:28:48 10-02-2024][INFO] Ping: 84.33 ms | HTTP/1.1 200 OK
[13:28:49 10-02-2024][INFO] Ping: 36.73 ms | HTTP/1.1 200 OK
[13:28:51 10-02-2024][INFO] Ping: 37.32 ms | HTTP/1.1 200 OK
[13:28:52 10-02-2024][INFO] Ping: 38.32 ms | HTTP/1.1 200 OK
```
