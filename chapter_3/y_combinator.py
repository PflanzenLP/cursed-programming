# this was the intended solution:
n = 4
while n < 50:
    n -= 3
    n *= 4
    n += 2
print(n)

# this was MY solution:
print("\n"+"\n".join(map(lambda n:f"Iteration {n}: {(lambda f,*a:f(f,*a))(lambda rec,n:4 if not n else rec(rec,n-1)+2*4**(n-1),n)}",range(5))))