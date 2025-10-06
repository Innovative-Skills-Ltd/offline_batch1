from abc import ABC, abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def send_money(self):
        pass

class bkash(PaymentGateway):
    def send_money(self):
        pass
    # def send_money(self,pin,longpress):
    #     print("this is bkash",pin,longpress)

class nexus_pay(PaymentGateway):
    pass
    # def send_money(self,pin,otp):
    #     print("this is bkash",pin,otp)

b_obj  = bkash()
# b_obj  = bkash().send_money(1234,'yes')
# nexus = nexus_pay().send_money(123,123456)