## --------------- Break & Continue ---------------

## Break
# If the break statement is inside a nested loop (loop inside another loop), the break statement will terminate the innermost loop.
# Use of break statement inside the loop

for val in "string":
    if val == "i":
        break; # Break outside the loop, dont finish iterating the sequence
    print(val);

print("The end");

## Continue
# The continue statement is used to skip the rest of the code inside a loop for the current iteration only

# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue; # if 'i' is found then skip this iteration and dont print it
    print(val);

print("The end");