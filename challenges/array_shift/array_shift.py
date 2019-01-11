def insertShiftArray(input_list, input_element):
    if len(input_list) % 2 == 0:
        mid = (len(input_list) // 2)
    else:
        mid = (len(input_list) // 2) + 1
    new_list = []
    counter = 0
    new_counter = 0
    while counter < len(input_list):
        if counter == mid:
            new_list += [input_element]
            mid = -1
            new_counter += 1
        else:
            new_list += [input_list[counter]]
            new_counter += 1
            counter += 1
    return new_list



# Following code will answer the problem with BIG O of 1/2 n
# answer = []

# for i in range(len(input_list)):
#   if len(input_list) - i == i:
#     answer.append(input_element)
#     return answer + input_list[i:]
  
#   elif len(input_list) % 2 == 1 and len(input_list) - i - 1 == i:
#     answer.append(input_element)
#     return answer + input_list[i:]
  
#   answer.append(input_list[i])
  
