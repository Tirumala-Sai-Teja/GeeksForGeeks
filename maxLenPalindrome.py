
N = 4
def performQueries(l, r, prefix):

	# 0-based indexing
	l -= 1
	r -= 1

	# Marks if there is an
	# odd frequency character
	flag = False

	# Length of the longest palindrome
	# possible from characters in range
	count = 0

	# Traverse for all characters
	# and count their frequencies
	for i in range(26):

		# Find the frequency in range 1 - r
		cnt = prefix[r][i]

		# Exclude the frequencies in range 1 - (l - 1)
		if (l > 0):
			cnt -= prefix[l - 1][i]

		# If frequency is odd, then add 1 less than
		# the original frequency to make it even
		if (cnt % 2 == 1):
			flag = True
			count += cnt - 1
		
		# Else completely add if even
		else:
			count += cnt
	
	# If any odd frequency character
	# is present then add 1
	if (flag):
		count += 1

	return count

# Function to pre-calculate the frequencies
# of the characters to reduce complexity
def preCalculate(s, prefix):

	n = len(s)

	# Iterate and increase the count
	for i in range(n):
		prefix[i][ord(s[i]) - ord('a')] += 1
	

	# Create a prefix type array
	for i in range(1, n):
		for j in range(26):
			prefix[i][j] += prefix[i - 1][j]
	
# Driver code
s = "amim"

# Pre-calculate prefix array
prefix = [[0 for i in range(26)]
			for i in range(N)]

preCalculate(s, prefix)

queries = [[1, 4] , [3, 4]]
q = len(queries)

# Perform queries
for i in range(q):
	print(performQueries(queries[i][0],
						queries[i][1],
						prefix))
	
# This code is contributed
# by mohit kumar
''' output:
3
1'''
