import array as arr
arraynum = arr.array('i',[1,3,5,3,7,9,3])
print("orginal array: "+str(arraynum))
print("number occurences of the number 3 in the said array:"+str(arraynum.count(3)))
arraynum.reverse()
print("reverse the order of the items:")
print(str(arraynum))
