
# Chocolate Distribution Problem
# arr[0..n-1] Represents Sizes Of Packets
# m Is Number Of Students.
# Returns Minimum Difference Between Maximum And Minimum Values Of Distribution.

def findMinDiff(arr, n, m):
	# If There Are No Chocolates Or Number Of Students Is 0
	if (m==0 or n==0):
		return 0
	# Sort The Given Packets
	arr.sort()
	# Number Of Students Cannot Be More Than Number Of Packets
	if (n < m):
		return -1
	# Largest Number Of Chocolates
	min_diff = arr[n-1] - arr[0]
	# Find The Subarray Of Size m Such That
	# Difference Between Last (Maximum In Case Of Sorted) And First (Minimum In Case Of Sorted) Elements Of Subarray Is Minimum.
	for i in range(len(arr) - m + 1):
		min_diff = min(min_diff , arr[i + m - 1] - arr[i])	
	return min_diff
# Driver Code
if __name__ == "__main__":
	arr = [45,48,92,80,100,47,44,5,58,20]
	m = 5
	n = len(arr)
	print("Minimum difference is", findMinDiff(arr, n, m))
	
