number=int(input("ente the number ti insert"))
num_list=list(range(1,number+1))
def my_filter(num_list):
    even_num=[]
    odd_num=[]
    for i in num_list:
        if i%5==0:
            if i%2==0:
                odd_num.append(i)
            else:
                even_num.append(i)
    return even_num,odd_num
output_value=my_filter(num_list)

print("List of numbers:",num_list)
print("List of Even numbers, which are multiples of 5 are:",output_value[0])
print("List of Odd numbers, which are multiples of 5 are:",output_value[1])
