A simple HTTP/HTTPS server pinger made in Python.

# Installation
Linux
```
git clone https://github.com/lilmond/httping/
cd httping
pip install -r requirements.txt
```

# Usage
```
python httping.py --help
```
```
usage: httping.py [-h] [-t TIMEOUT] [-nv] [-p PROXY] [-gr] [--header HEADERS] URL

A simple HTTP server pinger.

positional arguments:
  URL                   Target's full URL.

options:
  -h, --help            show this help message and exit
  -t TIMEOUT, --timeout TIMEOUT
                        Socket connection timeout value.
  -nv, --no-verify      Whether to verify SSL if the connection is HTTPS.
  -p PROXY, --proxy PROXY
                        Use proxy to ping? Type the address if so, example: socks5://127.0.0.1:9050
  -gr, --get-response   Whether to receive response header and body from the server and print it in the terminal.
  --header HEADERS      Add a custom header. Example: "--header Authorization: token123"
```

# Example
```
python httping.py https://www.roblox.com/login
```
```
[15:50:18 10-02-2024][INFO] Initializing HTTP Pinger on www.roblox.com:443...
[15:50:18 10-02-2024][INFO] (1) Ping: 49.66 ms | HTTP/1.1 200 OK
[15:50:20 10-02-2024][INFO] (2) Ping: 37.05 ms | HTTP/1.1 200 OK
[15:50:21 10-02-2024][INFO] (3) Ping: 36.09 ms | HTTP/1.1 200 OK
[15:50:23 10-02-2024][INFO] (4) Ping: 45.58 ms | HTTP/1.1 200 OK
```

# Example with Tor proxies

```
python httping.py http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/ -p socks5://127.0.0.1:9050
```
```
[15:45:03 10-02-2024][INFO] Initializing HTTP Pinger on 6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion:80...
[15:45:07 10-02-2024][INFO] (1) Ping: 3127.06 ms | HTTP/1.1 200 OK
[15:45:09 10-02-2024][INFO] (2) Ping: 452.95 ms | HTTP/1.1 200 OK
[15:45:11 10-02-2024][INFO] (3) Ping: 647.77 ms | HTTP/1.1 200 OK
[15:45:13 10-02-2024][INFO] (4) Ping: 621.05 ms | HTTP/1.1 200 OK
```
