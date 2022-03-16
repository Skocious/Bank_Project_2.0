class Account:

    def __init__(self, account_bal, customer_id, account_id):
        self.account_bal = account_bal
        self.customer_id = customer_id
        self.account_id = account_id

    def account_dict(self):
        return {
            "accountBal": self.account_bal,
            "customerId": self.customer_id,
            "accountId": self.account_id
        }

