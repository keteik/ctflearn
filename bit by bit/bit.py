operators = ["|", "&", "&", ">>", "|", "^", "^", "^", "&", "&", "|", "|", "~"]
string = ["b", "i", "n", "a", "r", "y", "r", "e", "f", "i", "n", "e", "r", "y"]

size = len(string)
nums = [] * size
for x in range(size):
	nums.append(pow(ord(string[x]), 3))

flag = nums[0]
for i in range(size -1):
	for x in range(i, size - 1):
		if(operators[x] == "|"):
			flag = flag | nums[x + 1]
		elif(operators[x] == "&"):
			flag = flag & nums[x + 1]
		elif(operators[x] == ">>"):
			flag = flag >> nums[x + 1]
		elif(operators[x] == "^"):
			flag = flag ^ nums[x + 1]
		elif(operators[x] == "~"):
			flag = ~flag 

print(flag)