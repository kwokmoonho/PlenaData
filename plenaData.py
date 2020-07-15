"""
# Author: Kwok Moon Ho
# Date: July 14 2020
# Company: Plena Data
# Time: 19 mins 42 sec
"""

#assume: no empty input and input is string.

def main():
    my_dict = {}
    my_list = []
    user_input = input("Please enter a string: ")
    for n in user_input:
        if my_dict.get(n.casefold()) == None:
            my_dict[n.casefold()] = 1
            my_list.append(n)
        else:
            my_dict[n] += 1
            if n.isupper():
                if (n in my_list):
                    my_list.pop(my_list.index(n.upper()))
                elif(n.lower() in my_list):
                    my_list.pop(my_list.index(n.lower()))
            elif n.islower():
                if n in my_list:
                    my_list.pop(my_list.index(n.lower()))
                elif n.upper() in my_list:
                    my_list.pop(my_list.index(n.upper()))
    #convert user_input ot list
    user_list = list(user_input)
    for q in my_list:
        if q in user_list:
            user_list.remove(q)
    #combine
    answer = my_list + user_list

    print("The final answer is: {}".format(''.join(answer)))

if __name__ == "__main__":
    main()
