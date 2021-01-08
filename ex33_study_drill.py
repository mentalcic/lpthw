start_number = input("give me starting number > ")
end_number = input("give me end number > ")
step_number = input("give me a stepping number > ")
numbers = []


def num_cruncher(start_no, end_no, step):
    if start_no > end_no:
        print(" Numbers do not match the requirement")
        return()
    else:
        i = start_no
        while i < end_no:
            print(f"At the top i is {i}")
            numbers.append(i)

            i = i + step
            print("Numbers now: ", numbers)
            print(f"At the bottom i is {i}")
            print('\n')
        return numbers


num_cruncher(int(start_number), int(end_number), int(step_number))

print("The numbers: ")

for num in numbers:
    print(num)
