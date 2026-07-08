import uuid

_orders_in_progress = {
    -1 : {
        "customer" : "test_login",
        "products" : [uuid.uuid4()]
    }
}

_registered_customers = {
    -1 : {
        "email"   : "mail@test.com",
        "address" : "ul. Testowa 1a"
    }
}
