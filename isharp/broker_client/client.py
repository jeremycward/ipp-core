
from isharp.broker_client.remote_proxy import BrokerConnectionPool
import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create console handler and set level to info
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger = logging.getLogger(__name__)


logger.info("hello from logging")


with BrokerConnectionPool() as broker:
    print(broker.checkout("file://nas174:5672/file_name_1.csv?format=CSV"))


print("end")


