good_list = []
print("Enter any text if you want to quit")
while True:
    nums = input("Enter numbers separated by space\n")
    bad_list = nums.split()
    try:
        for i in bad_list:
            good_list.append(float(i))
    except ValueError:
        print("Not a number")
        print(f"Summ is : {sum(good_list)}")
        break
    print(f"Summ is : {sum(good_list)}")