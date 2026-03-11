# From the CSV file in lesson 8

# 5 elements separated by ","
header = 'id,name,price,pic,store'

# if splitted by "," string0 and string1, the resulting list will have more than 5 elements
string0 ='33,"ACHVA TAHINI, 500 g",4.99,https://f.wishabi.net/page_items/362472784/1734779109/extra_large.jpg,NoFrills'
string1 ='48,"ACORN, BUTTERCUP, BUTTERNUT or SPAGHETTI SQUASH",1.77,https://f.wishabi.net/page_pdf_images/20060077/7a8e2b44-bf8b-11ef-a712-0ec6e2beadde/x_large,NoFrills'

strings = [string0, string1]

for idx, element in enumerate(strings):
    print(f"string{idx} has {len(element.split(","))} elements when splitted by ,")
    
# Possible solution
# split the strings by ", to get the the full name (" has to be escaped)

# elements, middle one full name
triple_list = string0.split("\"")

# we can split first and last elements by commas, and we will get undesireble elements:
# the last and the first respectively
l0 = triple_list[0].split(",")[0:-1]  # we avoid the last element
l1 = triple_list[1]  # it has the full name
l2 = triple_list[2].split(",")[1:]  # we discard the first element on index 0

print("\n","Cleaned up lists:", "\n")
print(l0)
print(l1)
print(l2)

final_list = l0

final_list.append(l1)
final_list.extend(l2)

print("\n", f"final list has {len(final_list)} elements")
print(final_list)

# making a function
def line_parser(line):
    triple_list = line.split("\"")
    
    l0 = triple_list[0].split(",")[0:-1]  # we avoid the last element
    l1 = triple_list[1]  # it has the full name
    l2 = triple_list[2].split(",")[1:]  # we discard the first element on index 0

    final_list = l0
    final_list.append(l1)
    final_list.extend(l2)
    
    return final_list

# testing on the sencond string
print("\n", "String1:")
next_string = line_parser(string1)
print(len(next_string))
print(next_string)