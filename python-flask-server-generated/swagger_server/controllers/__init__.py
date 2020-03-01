import threading
import logging

LOCK = threading.Lock()
logger = logging.getLogger("CERTBOT")
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
