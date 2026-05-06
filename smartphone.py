class Smartphone:
    def __init__(self, brand, model, subscriber_number):
        self.brand = brand
        self.model = model
        self.subscriber_number = subscriber_number

    def print_brand(self):
        print(self.brand)

    def print_model(self):
        print(self.model)

    def print_subscriber_number(self):
        print(self.subscriber_number)
