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
            candidq = max_revenue(n-i , prices) + max_revenue(i , prices)
            if candidq> maxq:
                maxq = candidq
        return candidq



def max_revenue_dp(n , prices):
    if n==0:
        return 0
    elif n==1:
        return prices[0]
    else:
        dp={0:0,1:prices[0]}
        for k in range(2,n+1):
            maxq = prices[k-1]
            for i in range(1,k):
                candidq = dp[k-i] + dp[i]
                if candidq> maxq:
                    maxq = candidq
            dp[k]=maxq
    return dp[n]

print(max_revenue_dp(10 , prices=[1,5,8,9,10,17,17,20,24,30]))

