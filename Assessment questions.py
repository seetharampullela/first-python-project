# find people which are present in both villages who are unique

village1 = input().split()
village2 = input().split()

result = []
for i in village1:
    for j in village2:
        if i == j:
            result.append(int(i))
            
print(list(set(result)))


# Given an array of integers and an integer target, return indices of the two numbers such that they
# add up to the target.
# You may assume that each input would have exactly one solution, and you may not use the same
# element twice.
# You can return the answer in any order. (using 2 for loop is not accepted).

# target = int(input())
# num_list = input().split()

# result = 0
# for i in num_list:
#     if 
# /


# Given an array A of non-negative integers, arrange them such that they form the largest number.
# Input -> [3, 30, 34, 5, 9]
# Output -> 9534330 - ( hard) - 10mins

list = [10,2,0]

new_list = []
for i in list:
    j=(i%10,i)
    new_list.append(j)
sorted_list = (sorted(new_list))

result = []

for j in sorted_list:
    result.append(str(j[1]))
new_result = result[::-1]
s=''
answer = (s.join(new_result))

print(int(answer))

# Given an integer n, return a string array answer (1-indexed) where:(FizzBuzz problem)
# ● answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# ● answer[i] == "Fizz" if i is divisible by 3.
# ● answer[i] == "Buzz" if i is divisible by 5.
# ● answer[i] == i (as a string) if none of the above conditions are true.
# Input: n = 5
# Output: [“1”,”2”,”Fizz”,”4”,”Buzz”,”Fizz”,”7”,”8”,”Fizz”,”Buzz”,”11”,”Fizz”,”13”,”14”,”FizzBuzz”]

n = int(input())
answer_string = []
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        answer_string.append("FizzBuzz")
    if i%3 == 0:
        answer_string.append("Fizz")
    if i%5==0:
        answer_string.append("Buzz")
    
    else:
        answer_string.append(str(i))
print(answer_string)

















N = int(input())
Years = N/365
Weeks = ((float(Years)-int(Years))*365)/7
Days = ((float(Weeks)-int(Weeks))*7)
Y = int(Years)
W = int(Weeks)
D = round(Days)
print(Y)
print(W)
print(D)