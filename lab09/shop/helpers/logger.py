import logging

logging.basicConfig(filename="shop.log")
shop_logger = logging.getLogger()
shop_logger.setLevel(logging.WARNING)
