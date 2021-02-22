import logging

def log_info(url, status_code, status, response_time):
    logging.info(f"{url:40} | status: {status_code} - {status:40} | response time: {response_time:>10} sec")