import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    3306: "MySQL"
}

def scan_ports(host):

    results = []

    for port, service in COMMON_PORTS.items():

        try:

            sock = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            )

            sock.settimeout(0.3)

            result = sock.connect_ex((host, port))

            if result == 0:

                results.append({
                    "port": port,
                    "service": service,
                    "status": "Open"
                })

            sock.close()

        except:
            pass

    return results