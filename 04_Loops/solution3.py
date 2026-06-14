num = 3

for i in range(1, 11):
    if i == 5:
        continue
    # the continue keyword will skip the rest of the code in the loop for the current iteration and move on to the next iteration
    print(num, "x", i, "=", num * i)
