from repositories.MainRepository import MainRepository


class CustomerLogic:

    def __init__(self):
        self.rep = MainRepository()

    
    def create(self, customer):
        self.rep.create_customer(customer)

    def get_all_customers(self):
        return self.rep.get_all_customers()

    def update(self, id, updates):
        return self.rep.update_customer(id, updates)

    def delete(self, id):
        return self.rep.delete_customer(id)

    def get_customer_by_id(self, id):
        customers = self.get_all_customers()

        for customer in customers:
            if customer.id == id:
                return customer
        return None





