import uuid
from .helpers.validation import _validate_order, _validate_customer_data
from .helpers.data import _orders_in_progress, _registered_customers
from .helpers.logger import shop_logger

def _register_customer(login, customer_data):
    if login in _registered_customers:
        return login
    try:
        _validate_customer_data(customer_data)
    except:
        raise
    _registered_customers[login] = customer_data
    return login

def _register_order(order):
    try:
        _validate_order(order)
    except:
        raise
    if order["customer"] not in _registered_customers:
        shop_logger.warning("the customer this order was assigned to is not registered!")
        raise KeyError("the customer this order was assigned to is not registered!")
    id = uuid.uuid4()
    _orders_in_progress[id] = order
    return id

def receive_order(order, new_customer_data=None):
    login = None
    if new_customer_data is not None :
        try:
            if not isinstance(new_customer_data, tuple) or len(new_customer_data) < 2:
                shop_logger.warning("new_customer_data was provided in an invalid form!")
                return (None, None)
            candidate_login, data = new_customer_data
            login = _register_customer(candidate_login, data)
        except Exception as e:
            shop_logger.warning(f"an error occurred while registering the new customer: {e}")
            login = None
    try:
        order_id = _register_order(order)
        if login is None:
            customer_from_order = order.get("customer") if isinstance(order, dict) else None
            login = customer_from_order
        return (login, order_id)
    except Exception as e:
        shop_logger.warning(f"an error occurred while registering the order: {e}")
        return (login, None)

def print_customers() :
    for k, v in _registered_customers.items() :
        print(k, v)

def print_orders() :
    for k, v in _orders_in_progress.items() :
        print(k, v)
