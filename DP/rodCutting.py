import sys
# sys.set_maximum_recursion_depth(100000)

def max_revenue_rec(n , prices):
    if n==0:
        return 0
    elif n==1:
        return prices[0]
    else:
        maxq = prices[n-1]
        for i in range(n):
            candidq = max_revenue_rec(n-i , prices) + max_revenue_rec(i , prices)
            if candidq> maxq:
                maxq = candidq
        return candidq

def calc_sol(sol , n , path=''):
    if n not in sol:
        return ''
    else:
        return "{}-{}-{}".format(calc_sol(sol , sol[n]-1) ,sol[n] , calc_sol(sol , n-sol[n]+1))


def max_revenue_dp(n , prices):
    if n==0:
        return 0
    elif n==1:
        return prices[0]
    else:
        dp={0:0,1:prices[0]}
        sol = {0:[] , 1:[1]}
        for k in range(2,n+1):
            maxq = prices[k-1]
            c = [k]
            for i in range(1,k):
                candidq = dp[k-i] + dp[i]
                if candidq> maxq:
                    maxq = candidq
                    c = sol[k-i] + sol[i]
            dp[k]=maxq
            sol[k] = c
    return dp[n] , sol[n]

print(max_revenue_dp(10 , prices=[10,5,8,9,20,17,17,20,24,30]))

