from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass

class WeChatPay(Payment):
    def pay(self,money):
        print('wechat')
    pass


pay = WeChatPay()
pay.pay(123)