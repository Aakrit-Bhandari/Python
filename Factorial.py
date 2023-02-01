import math
def fact(a):
    a_fact = 1
    for i in range(1,a+1):
        a_fact = a_fact*i
    return a_fact
n = int(input())
m = int(input())
n_fact = fact(n)
m_fact = fact(m)
n_m_fact = fact(n-m)
ans = n_fact//(m_fact*n_m_fact)
print(ans)
