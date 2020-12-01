def dict_1():
    class_list = dict() 
    data = input('Enter type & rate separated by ":" ') 
    temp = data.split(':') 
    class_list[temp[0]] = int(temp[1]) 
 
# Displaying the dictionary 
    for key, value in class_list.items(): 
        print('Name: {}, Score: {}'.format(key, value)) 

def dict_2():
    typ = input("Please input a type: ") 
    rate = input("Plesse input a rate: ") 
    class_list = {typ : rate}

    print (class_list)

dict_2()
