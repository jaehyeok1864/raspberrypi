# 4.function2.py

#Pascal, kebab ... 
#Camel case
sumResult
#Snake
sum_result = 10

def add_numbers(a, b):
    global sum_result  
    sum_result = a + b
    return sum_result

result = add_numbers(3, 5)
print(result)
print(sum_result) 
