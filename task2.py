# გააფართოვეთ სტანდარტულ ბიბლიოთეკაში არსებული მონაცემთა სტრუქტურა list.
# დაამატეთ მას ორი მეთოდი min და max, რომლებიც დააბრუნებენ მინიმალურ და მაქსიმალურ მნიშნელობას შესაბამისად.
# შექმენით კლასის რამდენიმე ობიექტი და აჩვენეთ რომ მოთხოვნილი ფუნქციონალი გამართულად მუშაობს.
# გამოიყენეთ მემკვიდრეობა.

class MinMax(list):
    def min(self):
        min_num = self[0]
        for num in self:
            if num < min_num:
                min_num = num

        return min_num


    def max(self):
        max_num = self[0]
        for num in self:
            if num>max_num:
                max_num=num

        return  max_num

my_list = MinMax()
my_list.append(2)
my_list.append(6)
my_list.append(100)
my_list.append(-100)
my_list.append(49)


print(my_list.min())
print(my_list.max())