def foo(end, step):
    i = 0
    numbers = []

    while i < end:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)


from sys import argv

script, end, step = argv
foo(int(end), int(step))
