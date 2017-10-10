class Myclass:

    visible_list = []
    visible_var = 'Joel'
    __hidden_variable = 0

    def add(self, increment):
        self.__hidden_variable += increment
        print(self.__hidden_variable)



obj = Myclass()
print(obj.visible_list)
## print(obj.__hidden_variable) throws error since hidden variable is not accessible/visible
obj.add(100)
obj.add(25)
obj.visible_list .append(255)
Myclass.visible_var += " Johnson"
print(obj.visible_list)
print(obj.visible_var)
obj1 = Myclass()
print(obj1.visible_list)
print(Myclass.visible_list)
print(obj1.visible_var)


