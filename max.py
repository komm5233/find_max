def find_max(a_list):
	if not a_list:
		return 0
	max_num = a_list[0] # 先宣告一個變數出來儲存"目前看過的最大數"，先設成清單中的第一個東西
	for line in a_list:
		if line > max_num:
			max_num = line
	return max_num 

print(find_max([1, 2, 3]))
print(find_max([1, -5, -1]))