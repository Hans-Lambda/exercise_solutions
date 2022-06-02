# https://www.edureka.co/blog/polymorphism-in-python/


class FlatRate:

    def __init__(self, fixed_amount):
        self.fixed_amount = fixed_amount
        self.description = "This is a flatrate..."

    def calculate(self, amount):
        return amount - self.fixed_amount


class VariableRate:

    def __init__(self, percentage):
        self.percentage = percentage    # 0.2 or 0.5...

    def calculate(self, amount):
        return amount - (amount * self.percentage)


class Client:

    def __init__(self, billing_strategy):
        self.billing_strategy = billing_strategy

    def generate_bill(self, total):
        return self.billing_strategy.calculate(total)


if __name__ == '__main__':

    variable_rate = VariableRate(0.2)
    fixed_rate = FlatRate(10)

    client1 = Client(fixed_rate)
    client2 = Client(variable_rate)

    print(client1.generate_bill(100))
    print(client2.generate_bill(200))

    client1.billing_strategy = variable_rate
    print(client1.generate_bill(100))
