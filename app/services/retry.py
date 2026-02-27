# Retry mechanism with exponential backoff
from tenacity import retry, stop_after_attempt, wait_exponential
from app.config import MAX_RETRIES

def retry_on_exception(func):

    @retry(
        stop=stop_after_attempt(MAX_RETRIES),
        wait=wait_exponential(multiplier=1, min=1, max=4),
        reraise=True
    )
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper