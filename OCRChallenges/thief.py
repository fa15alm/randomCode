def makeComboArray(num1, num2, num3, num4):
    array = []
    array.append(num1 + num2 + num3 + num4)
    array.append(num1 + num2 + num4 + num3)
    array.append(num1 + num3 + num2 + num4)
    array.append(num1 + num3 + num4 + num2)
    array.append(num1 + num4 + num2 + num3)
    array.append(num1 + num4 + num3 + num2)
    #######################################
    array.append(num2 + num1 + num3 + num4)
    array.append(num2 + num1 + num4 + num3)
    array.append(num2 + num3 + num1 + num4)
    array.append(num2 + num3 + num4 + num1)
    array.append(num2 + num4 + num1 + num3)
    array.append(num2 + num4 + num3 + num1)
    #######################################
    array.append(num3 + num1 + num2 + num4)
    array.append(num3 + num1 + num4 + num2)
    array.append(num3 + num2 + num1 + num4)
    array.append(num3 + num2 + num4 + num1)
    array.append(num3 + num4 + num1 + num2)
    array.append(num3 + num4 + num2 + num1)
    #######################################
    array.append(num4 + num1 + num2 + num3)
    array.append(num4 + num1 + num3 + num2)
    array.append(num4 + num2 + num1 + num3)
    array.append(num4 + num2 + num3 + num1)
    array.append(num4 + num3 + num1 + num2)
    array.append(num4 + num3 + num2 + num1)
    #######################################
    return array

while True:
    nums = input('List the 4 pin digits you know: ').strip()
    if len(nums) != 4:
        print('Please enter 4 digits. eg. \'1234\'.')
        continue
    else:
        try:
            nums = int(nums)
            nums = str(nums)
            break
        except ValueError:
            print('Please enter 4 digits. eg. \'1234\'.')
            continue

pinList = makeComboArray(nums[0], nums[1], nums[2], nums[3])
enter = input('Press enter to see the list of possible combinations.')
for pin in pinList:
    print(pin)
