 

def student(name,age,gender):
    print(f"Hey {name}!, you are {age} year old {gender} ")

student("Indrajeet",25,"male")
student("raj",24,"Male")


"""WAP to print square of number"""

def square(num):
    return num * num

num = int(input("Enter num : "))
print(square(num))



"""WAP to print minimum of three numbers"""

def min_of_three(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    return n3

n1 = int(input("Enter n1 :"))
n2 = int(input("Enter n2 :"))
n3 = int(input("Enter n3 :"))
print(min_of_three(n1,n2,n3))


"""WAP to print absolute value of given number"""

def absolute_value(num):
    if num > 0:
        return num
    return num * -1

print(absolute_value(-400))
print(absolute_value(-5))
print(absolute_value(393))


def is_sorted(lst):
    n = len(lst)
    for i in range(0,n-1):
        if lst[i] > lst[i + 1]:
            return "not Sorted"
    return "Sorted"

num = [3,6,21,34,53,59,69,83,90,95]
print(is_sorted(num))


"""WAP eligible for apply a driving licence """

def is_eligilbe(age):
    if age >=18 and age <=60 :
        return True
    else:
        return False

age = int(input("Enter your age : "))
if  0 < age <= 60:    
 if is_eligilbe(age):
    print("You are eligible to apply for licence")
 else :
    print(f"You need to wait for {18-age} years to apply for licence")
else:
   print("Age exceeds eligibility limit for licence")




"""WAP on who pays the bill between three of friends on age"""

def is_bill(jay_age,viru_age,gabbar_age):
   if jay_age > viru_age and jay_age > gabbar_age:
        return "Jay will pay the bill"
   elif viru_age > jay_age and viru_age > gabbar_age:
        return "Viru will pay the bill"
   else:
        return "Gabber will pay the bill" 
   

jay_age = int(input("Enter jay age : "))
viru_age = int(input("Enter Viru age : "))
gabbar_age = int(input("Enter Gabber age : "))

will_pay = is_bill(jay_age,viru_age,gabbar_age)
print(will_pay)

"""WAP to show Salary slip of an employee after HRA, DA, PF all this 
addtion in Basic salary """

def calculate_salary(basic_sal):
    HRA = (basic_sal*10)/100
    DA = (basic_sal*5)/100
    PF = (basic_sal*8)/100
    Total = basic_sal + HRA + DA + PF

    return HRA,DA,PF,Total 


def print_salary_slip(emp_name,basic_sal):
    HRA, DA, PF, Total = calculate_salary(basic_sal) 


    print("========== SALARY SLIP ===========")
    print("*"*40)
    print(f"Employee name : {emp_name}")
    print("="*40)
    print(f"Basic sal                      : {basic_sal}rs")
    print(f"HRA                            : {HRA}rs")
    print(f"DA                             : {DA}rs")
    print(f"PF                             : {PF}rs")
    print("-"*40)
    print(f"Total salary                   : {Total}rs")


emp_name =input("Enter emp name : ")
basic_sal = eval(input(f"Enter your basic Salary {emp_name} : "))

salary = print_salary_slip(emp_name,basic_sal)


"""WAP to print the given year is Leap year or not"""

def is_leap_year(year):
    if year % 4 ==0 and year % 400 or year % 100 == 0:
        return True
    return False

year = int(input("Enter year : "))

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


"""WAP to print discount on your purchase ammount greater than 5000 is 50%
   greater than 3000 is 30% and above 1000 only 10% """

def discount_of(purchase_amount):
    if purchase_amount > 5000:
        return purchase_amount*0.50
    elif purchase_amount > 2500:
        return purchase_amount*0.25
    elif purchase_amount > 1000:
        return purchase_amount*0.10
    else:
        return 0

purchase_amount = float(input("Enter purchased amount : "))

discount = discount_of(purchase_amount)
final_amount = purchase_amount-discount
if purchase_amount>1000:
    print(f"You will get an discount of {discount:.2f}INR and your payable amount is {final_amount:.2f}")
else:
    print("Sorry there is no discount for below 1000INR purchase")


"""WAP to print profir or loss on a buyed product after sell """

def profit_loss(buying_price,selling_price):
    if selling_price > buying_price:
        profit = selling_price - buying_price
        return f"Your are in profit of {profit}INR"
    elif buying_price > selling_price:
        loss = buying_price - selling_price
        return f"Yor in loss of {loss}INR"
    else :
        return "No profit no loss"
    
buying_price = int(input("Enter buying price : "))
selling_price = int(input("Enter the selling price : "))

print(profit_loss(buying_price,selling_price))


""" WAP to reverse a string """

def reverse(text):
    return text[::-1]

reversed = reverse("Indrajeet")
print(reversed)


"""WAP to reverse a list"""

def reverse(list):
    return list[::-1]

reversed = reverse(["Raj","Sai",10,True])
print(reversed)


"""WAP to print max, sum, min, len, avg, sort marks from list """

def max_mark(marks):
    avg = sum(marks)/len(marks)
    return max(marks),sum(marks),min(marks),len(marks),avg,sorted(marks)

res = max_mark([60,90,78,98,59])
print(res)

"""WAP to find and element from a list using indexing"""
def find_index(ele):
    return ele[-1][1]

name = find_index(["Sai","Rahul","Rohit","Sita","Gita","Ravi","Kumar"])
print(name)


"""WAP to print factors of given number"""

def fact(num):
   factors = []
   for i in range(1,num+1):
      if num % i == 0:
         factors.append(i)
      
   return factors

res = fact(10)
print(res)
