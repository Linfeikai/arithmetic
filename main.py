import random
from fractions import Fraction

ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

#用来生成数字
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

class Problem():
    '''存储每一道问题的类'''
    def __init__(self,expression = None,isValid = True,answer = ''):
        print('A blank pro has been generated.')
    #用来生成问题
    def makeProblem(self):
        # 随机数字的个数
        numbers = random.randint(2, 4)
        print('这个题目里有%d个数字' % numbers)
        # 生成这几个随机数 因为number等于3 所以要执行三次generate函数 把结果放在一个元组里面。
        numList = []
        for i in range(0, numbers):
            numList.append(generateNum())
        print('这些数字是：', numList)

        # 运算符号的个数等于随机数字个数减一
        sign = numbers - 1
        print('这个题目里有%d个运算符号' % sign)
        # 随机符号有哪些？
        signList = ['+', '-', '*', '÷']
        selectedSign = random.sample(signList, sign)
        print("这个运算符号是：", selectedSign)

        # 计算结果
        problem = ''
        # 现在我有两个元组 一个元组里面有n个元素 另一个元组里有n-1个元素 我要把这两个元组的元素依次读出来
        for a in range(0, len(selectedSign)):
            problem = problem + str(numList[a]) + ' ' + selectedSign[a] + ' '
        problem = problem + str(numList[len(numList) - 1])
        print(problem)
        self.description = problem
    #用来计算答案
    def caculate(self):
        expression = self.middle_to_after(self.description)
        self.answer = self.expression_to_value(self,expression)

    # 用来计算答案
    def middle_to_after(s):
        """
        中缀表达式转化后缀表达式.
        :param s: 中缀表达式的字符串表示，本程序中采用操作符跟数值之间用空格分开，例如:
        "9 + ( 3 - 1 ) * 3 + 10 / 2"
        :return: 后缀表达式，数组的形式，每个数值或者操作符占一个数组下标.
        """
        expression = []
        ops = []
        ss = s.split(' ')
        for item in ss:
            if item in ['+', '-', '*', '/']:  # 操作符
                while len(ops) >= 0:
                    if len(ops) == 0:
                        # 此时操作符栈里没有其他的运算符号，这是第一个运算符号，入栈
                        ops.append(item)
                        break
                    op = ops.pop()
                    if op == '(' or ops_rule[item] > ops_rule[op]:
                        # 比较要入栈的运算符号和当前栈顶元素的优先级
                        ops.append(op)
                        ops.append(item)
                        break
                    else:
                        expression.append(op)
            elif item == '(':  # 左括号，直接入操作符栈
                ops.append(item)
            elif item == ')':  # 右括号，循环出栈道
                while len(ops) > 0:
                    op = ops.pop()
                    if op == '(':
                        break
                    else:
                        expression.append(op)
            else:
                expression.append(item)  # 数值，直接入表达式栈

        while len(ops) > 0:
            expression.append(ops.pop())

        return expression

    def expression_to_value(self,expression):
        """
        :param expression: 后缀表达式的字符串表示，操作符跟数值间用空格分割，例如：
        "9 3 1 - 3 * + 10 2 / +"
        :return: 运算结果，一个值
        """
        stack_value = []
        for item in expression:
            if item in ['+', '-', '*', '/']:
                n2 = stack_value.pop()  # 注意，先出栈的在操作符右边.
                n1 = stack_value.pop()
                result = self.cal(self,n1,n2,item)
                stack_value.append(result)
            elif ('/' in item):
                # 如果压入的是分数
                item = Fraction(item)
                stack_value.append(item)  # 数值直接压栈.
            else:
                stack_value.append(int(item))
        return stack_value[0]

    def cal(self,n1, n2, op):
        if op == '+':
            return n1 + n2
        if op == '-':
            if(n1<n2):
                self.isValid=False
            return n1 - n2
        if op == '*':
            return n1 * n2
        if op == '/':
            if (n2 == 0 or n1 > n2):
                self.isValid = False
            return n1 / n2

mypro = Problem()
mypro.makeProblem()
mypro.caculate()
print(mypro.description,mypro.answer)

# myPro = Problem(1,2,3)
# myPro.makeProblem()
# myPro.caculate()
# print(myPro.caculate(),myPro.makeProblem())