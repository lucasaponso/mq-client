from dotenv import load_dotenv
import os

load_dotenv()

rabbit_mq_server_addr = os.getenv("RABBIT_MQ_SERVER_ADDR")