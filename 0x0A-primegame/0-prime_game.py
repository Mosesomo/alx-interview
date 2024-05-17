def isWinner(x, nums):
    '''Determines the overall winner after x rounds.'''
    if x < 1 or not nums:
        return None
    
    # Calculate primes up to the maximum number in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for num in nums:
        round_winner = play_round(num, primes)
        if round_winner:
            winnerCounter[round_winner] += 1
    
    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None

def sieve_of_eratosthenes(n):
    '''Returns a list of booleans indicating prime status up to n.'''
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    for start in range(2, int(n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, n + 1, start):
                is_prime[multiple] = False
    
    return is_prime

def play_round(n, primes):
    '''Plays a single round and returns the winner.'''
    list_nums = list(range(1, n + 1))
    players = ['Maria', 'Ben']
    current_player = 0  # Maria starts first

    # To keep track of which numbers have been removed
    removed = [False] * (n + 1)

    while True:
        # Find the smallest prime number still in the list
        prime_to_remove = -1
        for i in range(1, n + 1):
            if primes[i] and not removed[i]:
                prime_to_remove = i
                break

        # If no prime number can be found, current player loses
        if prime_to_remove == -1:
            return players[1 - current_player]
        
        # Remove the prime number and all its multiples
        for i in range(prime_to_remove, n + 1, prime_to_remove):
            removed[i] = True
        
        # Switch players
        current_player = 1 - current_player

