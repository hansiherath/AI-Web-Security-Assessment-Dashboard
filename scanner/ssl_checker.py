import ssl
import socket
from datetime import datetime

def check_ssl(hostname):

    try:

        context = ssl.create_default_context()

        with context.wrap_socket(
            socket.socket(),
            server_hostname=hostname
        ) as s:

            s.settimeout(5)

            s.connect((hostname, 443))

            cert = s.getpeercert()

            expiry = datetime.strptime(
                cert["notAfter"],
                "%b %d %H:%M:%S %Y %Z"
            )

            days_left = (expiry - datetime.now()).days

            issuer_org = "Unknown"

            for item in cert["issuer"]:

                if item[0][0] == "organizationName":

                    issuer_org = item[0][1]

                    break

            return {
                "Issuer": issuer_org,
                "Expiry Date": expiry.strftime("%Y-%m-%d"),
                "Days Remaining": days_left
            }

    except Exception as e:

        return {
            "Error": str(e)
        }