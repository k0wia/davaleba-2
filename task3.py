#შექმენით კლასი Animal, განუსაზღვრეთ ატრიბუტები სახელი და ასაკი. განუსაზღვრეთ მეთოდი info,
# რომელიც დააბრუნებს სრულ ინფორმაციას ობიექტის შესახებ. შექმენით კლასი Dog, რომელიც იქნება
# Animal კლასის მემკვიდრე. შეუქმენით ატრიბუტები, ჯიში და ფერი. ასევე განუსაზღვრეთ info მეთოდი,
# რომელიც დააბრუნებს სრულ ინფორმაციას ობიექტის შესახებ. შექმენით Dog კლასის რამდენიმე ობიექტი და აჩვენეთ რომ
# ფუნქციონალი გამართულად მუშაობს. დაიცავით ენკაფსულაციის პრინციპი.

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info1(self):
        print(f"name is {self.__name} and age is {self.__age}")



class Dog(Animal):
    def __init__(self,name, age ,breed, color , ):
        super().__init__(name , age)
        self.__breed= breed
        self.__color = color

    def info(self):
        print(f"breed is {self.__breed} , color is {self.__color}")

dog1 = Dog("bob" , 15, "labrador", "white")
dog2 = Dog("jeck" , 6, "bulldog", "black")

dog1.info1()
dog2.info1()
dog1.info()
dog2.info()
