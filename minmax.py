largest = -1
smallest=-1


while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        n = float(num)
#min=smallest
    except:
        print("Invalid input")
        continue
    if num == "done":
        break
    elif n > largest:
        largest = n
    elif n < smallest:
        smallest = n
        min=smallest


print("Maximum is", largest)
print("Minimum is", smallest)