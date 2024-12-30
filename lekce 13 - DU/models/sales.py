class Sales:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Sales, cls).__new__(cls, *args, **kwargs)
            cls._instance.sales_data = []
        return cls._instance

    def record_sale(self, order):
        self.sales_data.append(order)

    def total_sales(self):
        return sum(order.total_price() for order in self.sales_data)
