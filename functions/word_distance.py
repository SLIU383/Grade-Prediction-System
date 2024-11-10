def edit_distance_word(str1, str2):
    """
    Calculate the edit distance between two words.

    Args:
        str1 (str): The first word.
        str2 (str): The second word.

    Returns:
        int: The edit distance between the two words.
    """
    m, n = len(str1), len(str2)
        
    # Initialize a 2D array to store the edit distance values
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp array using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      
                                   dp[i][j - 1],      
                                   dp[i - 1][j - 1])  
    
    # Return the minimum edit distance
    return dp[m][n]