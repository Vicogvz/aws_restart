"""
Lab 5
"""
myMixedTypeList = [45, 290578, 1.02, True, "\"My dog is on the bed.\"", "\"45\""]

for item in myMixedTypeList:
    print(f"{item} is of the data type: {type(item)}")

print(f"La variable myMixedType es de tipo: {type(myMixedTypeList)}")