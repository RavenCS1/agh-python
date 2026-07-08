import json

class SalesReport:

    def __init__(self, filename):
        self.filename = filename

    def load_orders(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def total_sales(self):
        orders = self.load_orders()

        return sum(
            # order["price"]
            order["price"] * order["quantity"]
            for order in orders
        )

    def average_order_value(self):
        orders = self.load_orders()

        if not orders:
            return 0

        return self.total_sales() / len(orders)

    def best_selling_product(self):
        orders = self.load_orders()

        if not orders:
            return None

        counts = {}

        for order in orders:
            counts[order["product"]] = (
                counts.get(order["product"], 0)
                + order["quantity"]
            )

        return max(
            counts,
            key=counts.get
        )

    def orders_by_customer(self, customer):
        orders = self.load_orders()

        return [
            order
            for order in orders
            if order["customer"].lower()
            == customer.lower()
        ]

    def add_order(self, order):
        if order["quantity"] <= 0 or order["price"] <= 0:
            raise ValueError
        
        orders = self.load_orders()

        orders.append(order)

        # For testing purposes I wanted the original file to stay untouched,
        # so tests are easily repeatable without needing to remove the added
        # entries from the file, so I write the modified whole to a
        # different file
        new_file_name = "Appended" + self.filename

        with open(new_file_name, "w") as f:
            json.dump(orders, f)

        return orders