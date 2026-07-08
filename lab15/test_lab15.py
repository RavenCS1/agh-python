import pytest
import lab15

class TestLab15:
    def setup_method(self):
        self.instance = lab15.SalesReport("test.json")
        self.empty = lab15.SalesReport("empty.json")
    
    def teardown_method(self):
        del self.instance
        del self.empty

    def test_total_sales_working(self):
        assert self.instance.total_sales() == 6300

    def test_average_order_value(self):
        assert self.instance.average_order_value() == 6300 / 2
        assert self.empty.average_order_value() == 0

    def test_best_selling_product(self):
        assert self.instance.best_selling_product() == "Mouse"
        assert self.empty.best_selling_product() is None

    def test_orders_by_customer(self):
        assert self.instance.orders_by_customer("Alice") == [
            {
                "id": 1,
                "customer": "Alice",
                "product": "Laptop",
                "quantity": 2,
                "price": 3000
            }
        ]
        assert self.instance.orders_by_customer("Bob") == [
            {
                "id": 2,
                "customer": "Bob",
                "product": "Mouse",
                "quantity": 3,
                "price": 100
            }
        ]
        assert self.instance.orders_by_customer("ALICE") == self.instance.orders_by_customer("Alice")
        assert self.instance.orders_by_customer("alice") == self.instance.orders_by_customer("Alice")
        assert self.empty.orders_by_customer("Alice") == []
        assert self.empty.orders_by_customer("Bob") == []

    def test_add_order(self):
        assert self.instance.add_order(
                {
                    "id": 3,
                    "customer": "Tom",
                    "product": "Keyboard",
                    "quantity": 4,
                    "price": 50
                }) == [{"id": 1, "customer": "Alice", "product": "Laptop", "quantity": 2, "price": 3000}, {"id": 2, "customer": "Bob", "product": "Mouse", "quantity": 3, "price": 100}, {"id": 3, "customer": "Tom", "product": "Keyboard", "quantity": 4, "price": 50}]

        with pytest.raises(ValueError):
            self.instance.add_order(
                {
                    "id": 3,
                    "customer": "Tom",
                    "product": "Keyboard",
                    "quantity": 0,
                    "price": 1
                })
        with pytest.raises(ValueError):
            self.instance.add_order({
                    "id": 3,
                    "customer": "Tom",
                    "product": "Keyboard",
                    "quantity": -1,
                    "price": 1
                })
        with pytest.raises(ValueError):
            self.instance.add_order({
                    "id": 3,
                    "customer": "Tom",
                    "product": "Keyboard",
                    "quantity": 1,
                    "price": 0
                })
        with pytest.raises(ValueError):
            self.instance.add_order({
                    "id": 3,
                    "customer": "Tom",
                    "product": "Keyboard",
                    "quantity": 1,
                    "price": -1
                })
        with pytest.raises(ValueError):
            self.instance.add_order({
                    "id": 4,
                    "customer": "Kate",
                    "product": "Headphones",
                    "quantity": 0,
                    "price": 0
                })
        with pytest.raises(ValueError):
            self.instance.add_order({
                    "id": 4,
                    "customer": "Kate",
                    "product": "Headphones",
                    "quantity": -1,
                    "price": -1
                })
