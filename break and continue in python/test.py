for i in range(12):
    if i == 10:
        # break statement is used to exit the loop when the condiiton is true
        break 
    print("5 x", i+1, "=", 5*(i+1))

    
for i in range(1,12):
    if i ==10:
        # continue statemnet is used to skip the current iteration when the condition is true and continue with the next iteration
        continue
    print("5 x", i, "=", 5*i)