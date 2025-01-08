class Sales:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sales, cls).__new__(cls, *args, **kwargs)
            cls._instance.sales_data = []
        return cls._instance

    def record_sale(self, order):
        self.sales_data.append(order)
        from utils.parser import OrderParser
        try:
            OrderParser.write_orders_to_file(self.sales_data)
        except FileNotFoundError:
            print("Creating new orders.json file.")
            OrderParser.write_orders_to_file(self.sales_data)

    def reset_sales(self):
        self.sales_data = []

    def total_sales(self):
        return sum(order.total_price() for order in self.sales_data)

    def detailed_sales(self):
        if not self.sales_data:
            return "No sales recorded yet."
        result = []
        for i, order in enumerate(self.sales_data, start=1):
            result.append(f"Order {i}:")
            for pizza in order.pizzas:
                toppings = ", ".join([topping.name for topping in pizza.toppings]) or "No toppings"
                result.append(f"  - {pizza.size.capitalize()} {pizza.name} - {pizza.price} CZK (Toppings: {toppings})")
            result.append(f"  Total: {order.total_price()} CZK")
            result.append(f"  Payment Method: {order.get_payment_method()}\n")
        result.append(f"Overall Sales Total: {self.total_sales()} CZK")
        return "\n".join(result)