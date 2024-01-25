#Q1. the expected output of the following Python code given below:#

data= [10, 501, 22, 37, 100, 999, 87, 351] #Code given
result= filter (lambda x: x > 4, data)# x > 4 check in data
print(list(result))  

#Output- [10, 501, 22, 37, 100, 999, 87, 351]


#Q2. a python code using Lambda function to check every element of a list is an Integer or String?#

my_list= [5, 9, 'fruit', 'vegetable']

# Lambda function to check if an element is an Integer or String
new= lambda x: 'Integer' if isinstance(x, int) else 'String'

# Applying the lambda function using map to each element in my_list
result = list(map(new, my_list))

print(result)

#Output- ['Integer', 'Integer', 'String', 'String']


#Q3. Python lambda function create a Fibonacci series from 1 to 50 elements?#

from functools import reduce
# Number of elements in the Fibonacci series
elements = 50

# Lambda function to generate Fibonacci series
fibonacci_reduce = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n-1), [0, 1])

# Applying the lambda function to get the Fibonacci series
fibonacci_series_reduce = fibonacci_reduce(elements)

print(fibonacci_series_reduce)

#Output- [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025]


#Q4.a) write a python function to validate the Regular Expression for the following:#

import re

valid_Email= "sunishalazarus@yahoo.com"

# Regular expression pattern for basic email validation
email_pattern= '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+[a-zA-Z]{2,}$'
result= re.match(email_pattern, valid_Email)

# Check the result and print 
if result:
    print(f"{valid_Email} is a valid email address.")
else:
    print(f"{valid_Email} is not a valid email address.")

#Output- sunishalazarus@yahoo.com is a valid email address.
    

#Q4.b) write a python function to validate the Regular Expression for the following:#
    
import re

valid_bangladesh_mobile_number= '01918345279'

# Regular expression pattern for mobile validation
mobile_pattern= '^01[3-9]\d{8}$'
result= re.match(mobile_pattern, valid_bangladesh_mobile_number)

# Check the result and print 
if result:
    print(f"{valid_bangladesh_mobile_number} is a valid mobile number of Bangladesh.")
else:
    print(f"{valid_bangladesh_mobile_number} is not a valid mobile number of Bangladesh.")

#Output- 01918345279 is a valid mobile number of Bangladesh.
    

#Q4.c) write a python function to validate the Regular Expression for the following:#
    
import re

valid_usa_telephone_number= "(555) 587-3589"

# Regular expression for USA telephone numbers
phone_pattern= '^\d{3}\)\s?|\d{3}$'
result= re.findall(phone_pattern, valid_usa_telephone_number)

# Check the result and print 
if result:
    print(f"{valid_usa_telephone_number} is a valid telephone number of USA.")
else:
    print(f"{valid_usa_telephone_number} is not a valid telephone number of USA.")

#Output- (555) 587-3589 is a valid telephone number of USA.


#Q4.d) write a python function to validate the Regular Expression for the following:#
    
import re

valid_password= 'Afgh4879!@#$5658'

# Regular expression for a 16-character alpha-numeric password
password_pattern= '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$])[A-Za-z0-9!@#$]{16,}$'
result= re.match(password_pattern, valid_password)

# Check the result and print 
if result:
    print(f"{valid_password} is a valid 16-character alpha-numeric password.")
else:
    print(f"{valid_password} is not a valid 16-character alpha-numeric password.")

#Output- Afgh4879!@#$5658 is a valid 16-character alpha-numeric password.




