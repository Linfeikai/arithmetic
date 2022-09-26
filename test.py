import random
from fractions import Fraction

#生成数字
def generateNum():
#对每一个要运算的数，它是整数、带分数、真分数的概率是相等的。
   a = random.randint(0,2)
#生成整数
   if(a==0):
       return (random.randint(0,9))
#生成小数
   elif(a==1):
       denominator = random.randint(2, 20)
       numerator = random.randint(1, denominator)
       frac = Fraction(numerator, denominator)
       return frac
       # return (random.random())
#生成带分数
   elif(a==2):
       denominator = random.randint(1, 20)
       numerator = random.randint(denominator, denominator*3)
       frac = Fraction(numerator, denominator)
       return frac
#把中继表达式转换成后继表达式
# def middleToAfter():


#随机生成一个小数 0~1之间
# print(random.random())
#随机生成a-b之间的整数 闭区间
# print(random.randint(1,2))
#生成a-b之间的小数
# print(random.uniform(1.1,3.3))
'''
    已知 题目数量，每个数字最大不能超过几，
    要生成：比如说 生成一道题 每个数字最大不能超过10
    要确定：要有几个数字？最大不能多于三个运算符号，也就是数字不能多于4个
    可以：随机符号的个数，或者随机数字的个数
'''
#随机数字的个数
numbers = random.randint(2,4)
print('这个题目里有%d个数字' %numbers)
#生成这几个随机数 因为number等于3 所以要执行三次generate函数 把结果放在一个元组里面。
numList = []
for i in range(0,numbers):
    numList.append(generateNum())
print('这些数字是：',numList)


#运算符号的个数等于随机数字个数减一
sign = numbers - 1
print('这个题目里有%d个运算符号' %sign)

#随机数字是哪些

#随机符号有哪些？
signList = ['+','-','*','÷']
selectedSign = random.sample(signList,sign)
print("这个运算符号是：",selectedSign)

#计算结果
problem = ':'
# 现在我有两个元组 一个元组里面有n个元素 另一个元组里有n-1个元素 我要把这两个元组的元素依次读出来
for a in range(0,len(selectedSign)):
    problem = problem + str(numList[a]) + ' ' +selectedSign[a] + ' '
problem = problem + str(numList[len(numList)-1])
print(problem)
#
# x = Fraction(1,2)
# y = Fraction(2,3)
# z = x*y*3
# print(z)
# d = random.randint(1,20)
# f = random.randint(1,d)
# e = Fraction(f,d)
# print(e)
#加法
a = Fraction('4/5')
print(type(a))
print(a)