str_to_be_reversed = input("Input a string to reverse > ")

"""
python not support str item assignment
"""

# len_of_str = len(str_to_be_reversed)
# for i in range(int(len_of_str/2)):
#     i_opposite = len_of_str-1-i
#     str_to_be_reversed[i], str_to_be_reversed[i_opposite] = str_to_be_reversed[i_opposite], str_to_be_reversed[i]

print("Reversed string is : ", str_to_be_reversed[::-1])
