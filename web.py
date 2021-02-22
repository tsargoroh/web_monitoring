import requests
import log

def request(url, requirements_list):
    try:
        response = requests.get(url, timeout=5)
    #In the event of a network problem (e.g. DNS failure, refused connection, etc),
    #Requests will raise a ConnectionError exception
    except requests.exceptions.Timeout:
        log.log_info(url, "N/A", "timeout", "N/A")
        return (True, "N/A", "timeout", "N/A")
    except requests.exceptions.ConnectionError:
        log.log_info(url, "N/A", "connection error", "N/A")
        return (True, "N/A", "connection error", "N/A")
    else:
        status_code = response.status_code
        #The Response object as returned by requests.get() has a property called elapsed,
        #which gives the time delta between the request was sent and the response was received
        response_time = response.elapsed.total_seconds()
        if (status_code >= 200 and status_code < 400):
            for requirement in requirements_list:
                if (requirement.lower() in response.text.lower()):
                    pass
                else:
                    log.log_info(url, status_code, "content requirements were not fulfilled", response_time)
                    return (True, status_code, "content requirements were not fulfilled", response_time)
            else:
                log.log_info(url, status_code, "matches all content requirements", response_time)
                return (False, status_code, "matches all content requirements", response_time)
        elif (status_code >= 400 and status_code < 500):
            log.log_info(url, status_code, "client error", response_time)
            return (True, status_code, "client error", response_time)
        elif (status_code >= 500):
            log.log_info(url, status_code, "server error", response_time)
            return (True, status_code, "server error", response_time)