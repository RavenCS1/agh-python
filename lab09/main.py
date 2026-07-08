import uuid

orders = [
    {
        "customer": ("zosia", {"email": "zosia@newmail.com", "address": "ul. Radosna 4"}),
        "order": {
            "customer": "zosia",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": ("zosia", {"email": "zosia@newmail.com", "address": "ul. Radosna 4"}),
        "order": {
            "customer": "zosia",
            "products": [uuid.uuid4(), uuid.uuid4(), uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "zosia",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "arek",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": ("tomek", {"email": "tomek@example.org", "address": "ul. Leśna 5"}),
        "order": {
            "customer": "tomek",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "arek",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": ("basia", {"email": "basia@fresh.com", "address": "ul. Spacerowa 99"}),
        "order": {
            "customer": "basia",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "tomek",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "ola92",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": ("basia", {"email": "basia@fresh.com", "address": "ul. Spacerowa 99"}),
        "order": {
            "customer": "basia",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": None,
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "arek",
            "products": ["not-a-uuid"]
        }
    },
    {
        "customer": None,
        "order": "this should be a dict"
    },
    {
        "customer": None,
        "order": {
            "products": [uuid.uuid4(), uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "jurek"
        }
    },
    {
        "customer": ("halina",),
        "order": {
            "customer": "halina",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": ("wojtek", {"address": "ul. Słoneczna 8"}),
        "order": {
            "customer": "wojtek",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": ("zosia", {"email": "zosia@newmail.com", "address": ""}),
        "order": {
            "customer": "zosia",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "nowak",
            "products": [uuid.uuid4()]
        }
    },
    {
        "customer": None,
        "order": {
            "customer": "karolina",
            "products": []
        }
    }
]


import shop


print("initial state")
shop.print_customers()
shop.print_orders()


for entry in orders:

    print(f"adding: {entry}")
    print(shop.receive_order(entry["order"], entry["customer"]))
    print()


print("state after filling")
shop.print_customers()
shop.print_orders()
