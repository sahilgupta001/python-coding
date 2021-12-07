# ab ye comments samajhna aaram se khud se me khud koi comment add ni kar rha
# ni samajh ayega to fir me comments add karuga
# har progran me har line ke baad print daalke zarur samjha kar
# varna aaj tak ka kia karaya sab waste hojayega
# ye sab bhot dhyaan se kario

def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n-1):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j + 1] :
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("% d" % arr[i]),
