# a=14
# b=3
# c=a+b
# d=a-b
# e=a*b
# f=a/b
# g=a//b
# print(f)
# h=a%b
# print(h)
# for i in range (10):
#     print(i)
# total=0
# for i in range(1,15):
#     total=total+i
# print(total)

# s = 4.3
# steps = 0
# current = 2
# total = 0
# while total < s:
#     steps += 1
#     total += current
#     current *= 0.98
# print(steps)

# var1='holle world!'
# var2="Runoob"
# print("var[0]:",var1[0])
# print("var2[1:5]:",var2[1:5])

# var1 = 'Hello World!'
# var2 = "Runoob"
#
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])

#total=0
# for i in range(0,n):
#     total+=numbers[i]
# print(total)
#number=n
# hasFactor=0 
# for i in range(2,number):
#     if number %i==0:
#         hasFactor=1
#
# if hasFactor ==0:
#     print("it is prime")
# else:
#     print("it is not")
# numbers=[4,2,1,9,10]
# n=len(numbers)
# for i in range(0,n):
#      print(numbers[i])
# hasFactor=0
# for i in range(2,n):
#     if n %i==0:
#         hasFactor=1
# if hasFactor==0:
#     print("it is prime")
# else:
#     print("it is not")
for i in range(0,n):
    hasFactor=0
    for j in range(2,numbers[i]):
        if numbers[i]%j=0:
            hasFactor=1
            if hasFactor==0:
                print(numbers[i])