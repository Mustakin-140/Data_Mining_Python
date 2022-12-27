def Average(ob):
	sum_of_ob = 0
	for i in range(len(ob)):
		sum_of_ob += ob[i]
	average = sum_of_ob/len(ob)
	return average
ob = [6,11,2,0,1,6,16,6,6,3]
average = Average(ob)
print("Average of the list =", round(average, 2))
