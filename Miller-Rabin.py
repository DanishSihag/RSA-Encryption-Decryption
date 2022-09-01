def a_d_test(a,d,p):
    if pow(a,d)%p==1:
        return True
    else:
        return False

def a_2i_d_test(a,d,p,s):
    for i in range(s):
        if pow(a,pow(2,i)*d)%p == p-1:
            return True
    return False

def determining_s_d(p,a):
    x=p-1
    s=0
    while True:
        if(x%2==0):
            x=x//2
            s=s+1
        if(x%2!=0):
            d=p
            break
    if a_d_test(a,d,p):
        print("possibly prime")
    if a_2i_d_test(a,d,p,s):
        print("possibly prime")
    print("composite number")

print(determining_s_d(561,2))
