from urllib.parse import urlparse
import argparse
import logging
import socket
import time
import ssl

def main():
    parser = argparse.ArgumentParser(description="A simple HTTP server pinger.")
    parser.add_argument("url", metavar="URL", type=str, help="Target's full URL.")
    parser.add_argument("-t", "--timeout", metavar="TIMEOUT", type=int, default=5, help="Socket connection timeout value.")
    parser.add_argument("-nv", "--no-verify", action="store_true", default=False, help="Whether to verify SSL if the connection is HTTPS.")
    args = parser.parse_args()

    parsed_url = urlparse(args.url)

    if not parsed_url.port:
        if parsed_url.scheme == "https":
            port = 443
        else:
            port = 80
    else:
        port = parsed_url.port

    hostname = parsed_url.hostname

    socket.setdefaulttimeout(args.timeout)
    
    logging.basicConfig(
        format="[%(asctime)s][%(levelname)s] %(message)s",
        datefmt="%H:%M:%S %m-%d-%Y",
        level=logging.INFO
    )

    logging.info(f"Initializing HTTP Pinger on {hostname}:{port}...")

    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connect_time = time.time()
            sock.connect((hostname, port))
            connected_time = time.time()
            connection_timestamp_ms = f"{((connected_time - connect_time) * 1000):.2f}"

            if parsed_url.scheme == "https":
                ctx = ssl.create_default_context()
                if args.no_verify:
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.VerifyMode.CERT_NONE
                    sock = ctx.wrap_socket(sock=sock)
                else:
                    sock = ctx.wrap_socket(sock=sock, server_hostname=hostname)

            http_headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "en-US,en;q=0.9",
                "connection": "keep-alive",
                "dnt": "1",
                "host": f"{hostname}{':' + port if not port in [80, 443] else ''}",
                "sec-ch-ua": "\"Microsoft Edge\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "none",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
            }

            http_header = f"GET {parsed_url.path} HTTP/1.1\r\n"

            for header in http_headers:
                http_header += f"{header}: {http_headers[header]}\r\n"
            
            http_header += "\r\n"

            sock.send(http_header.encode())

            first_line = b""

            while True:
                chunk = sock.recv(1)

                if not chunk:
                    raise Exception("Connection closed unexpectedly.")
                
                first_line += chunk

                if first_line.endswith(b"\r\n"):
                    break

            logging.info(f"Ping: {connection_timestamp_ms} ms | {first_line.decode().strip()}")

            time.sleep(1)
        except Exception as e:
            logging.info(f"ERROR: {e}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
