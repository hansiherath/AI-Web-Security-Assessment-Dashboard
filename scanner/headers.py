import requests

SECURITY_HEADERS = {
    "Content-Security-Policy": "High",
    "Strict-Transport-Security": "High",
    "X-Content-Type-Options": "Medium",
    "X-Frame-Options": "Medium",
    "Referrer-Policy": "Low"
}

def check_headers(url):

    try:

        response = requests.get(
            url,
            timeout=5,
            allow_redirects=True
        )

        results = {}

        for header, severity in SECURITY_HEADERS.items():

            if header in response.headers:
                results[header] = {
                    "status": "Present",
                    "severity": "Info"
                }

            else:
                results[header] = {
                    "status": "Missing",
                    "severity": severity
                }

        return results

    except Exception as e:
        return {"Error": str(e)}