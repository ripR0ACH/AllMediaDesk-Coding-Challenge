# name: Zachary Morrison


import sys
import matplotlib.pyplot as plt

# Part 1: create a term calculator that starts with 
#         a string representing a mathmatical 
#         calculation to be performed, parse it, then
#         return the result of the calculation
def solve(exp):
    operator = ["+", "-", "*", "/"]
    exp_arr = []
    if len(exp) == 0:
        return 0
    op = "+"
    num = 0
    i = 0
    while i < len(exp):
        chr = exp[i]
        if chr.isdigit():
            num = num * 10 + int(chr)
        
        if chr == '(':
            length = 0
            end = 0
            copy = exp[i:]
            while end < len(copy):
                if copy[end] == "(":
                    length += 1
                elif copy[end] == ")":
                    length -= 1
                    if length == 0:
                        break
                end += 1
            num = solve(exp[i + 1:i + end])
            i += end
        if i + 1 == len(exp) or chr in operator:
            if op == operator[0]:
                exp_arr.append(num)
            elif op == operator[1]:
                exp_arr.append(-num)
            elif op == operator[2]:
                exp_arr[-1] = exp_arr[-1] * num
            elif op == operator[3]:
                exp_arr[-1] = exp_arr[-1] / float(num)
            op = chr
            num = 0
        i +=1
    return sum(exp_arr)    

def main():
    exp = input("Input a mathematical expression: ")
    if "y =" in exp or "y=" in exp:
        if "x" in exp or "X" in exp:
            x = [x - 5 for x in range(0, 11)]
            y = [solve(exp.replace("x", str(num))) for num in x]
            plt.plot(x, y, marker = 'o')
            plt.xlabel('x - axis')
            plt.ylabel('y - axis')
            plt.title('graph of y vs x')
            plt.show()
    else:
        print("The expression:\n" + exp + " = " + str(solve(exp)))

if __name__ == "__main__":
    main()