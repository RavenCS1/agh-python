import uuid
from ..helpers.logger import shop_logger

def _validate_order(order) :
    if(not isinstance(order, dict)) :
        shop_logger.warning("order should be of type dict!")
        raise TypeError("order should be of type dict!")
    if("customer" not in order.keys()) :
        shop_logger.warning("order should have a 'customer' key!")
        raise KeyError("order should have a 'customer' key!")
    if(not isinstance(order["customer"], str)) :
        shop_logger.warning("field order['customer'] should be of type str!")
        raise TypeError("field order['customer'] should be of type str!")
    if(order["customer"] == "") :
        shop_logger.warning("field order['customer'] cannot be empty!")
        raise ValueError("field order['customer'] cannot be empty!")
    if("products" not in order.keys()) :
        shop_logger.warning("order should have a 'products' key!")
        raise KeyError("order should have a 'products' key!")
    if(not isinstance(order["products"], list)) :
        shop_logger.warning("field order['products'] should be of type list!")
        raise TypeError("field order['products'] should be of type list!")
    if(not order["products"]) :
        shop_logger.warning("field order['products'] cannot be empty!")
        raise ValueError("field order['products'] cannot be empty!")
    if(not all(isinstance(id, uuid.UUID) for id in order["products"])) :
        shop_logger.warning("elements of field order['products'] should be of type uuid.UUID!")
        raise TypeError("elements of field order['products'] should be of type uuid.UUID!")

def _validate_customer_data(data) :
    if(not isinstance(data, dict)) :
        shop_logger.warning("data should be of type dict!")
        raise TypeError("data should be of type dict!")
    if("email" not in data.keys()) :
        shop_logger.warning("data should have an 'email' key!")
        raise KeyError("data should have an 'email' key!")
    if(not isinstance(data["email"], str)) :
        shop_logger.warning("field data['email'] should be of type str!")
        raise TypeError("field data['email'] should be of type str!")
    if(data["email"] == "") :
        shop_logger.warning("field data['email'] cannot be empty!")
        raise ValueError("field data['email'] cannot be empty!")
    if("address" not in data.keys()) :
        shop_logger.warning("data should have an 'address' key!")
        raise KeyError("data should have an 'address' key!")
    if(not isinstance(data["address"], str)) :
        shop_logger.warning("field data['address'] should be of type str!")
        raise TypeError("field data['address'] should be of type str!")
    if(data["address"] == "") :
        shop_logger.warning("field data['address'] cannot be empty!")
        raise ValueError("field data['address'] cannot be empty!")
