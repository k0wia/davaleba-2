#შექმენით CallMixin კლასი რომელსაც ექნება ერთი მეთოდი call. შექმენით კლასი Person,
# განუსაზღვრეთ შემდეგი ატრიბუტები fname, lname, phone. განუსაზღვრეთ მეთოდი info.
# CallMixin კლასის გამოყენებით, Person კლასს დაამატეთ დარეკვის ფუნქციონალი.

class Person:
    def __init__(self, fname, lname, phone):
        self.fname =  fname
        self.lname = lname
        self.phone = phone


class CallMixin:
    def call(self):
        print(f"calling {self.fname} {self.lname} on number {self.phone}")


class Contact(CallMixin, Person):
    pass

person1 = Contact("kote", "arsenashvili", 2322113)
person1.call()