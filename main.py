
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************

# print ('True') or print ('False')
count = 0
for n in num2:
    if n in num1:
        count += 1

if count == len(num2):
    print(True)
else:
    print(False)
