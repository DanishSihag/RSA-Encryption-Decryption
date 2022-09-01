from ext_euc import ext_euc
def chin_rem(p,q,c,e):
    n=p*q

    gcd,d,y=ext_euc(e,(p-1)*(q-1))                   #getting the simplification for d.e=1mod(phi(n))
    print(f"value of d now = {d}")
    d=d%((p-1)*(q-1))                                #from online notes, to get actual updated value of d
    print(f"actual updated value of d = {d}")

    dp=d%(p-1)
    dq=d%(q-1)

    mp=pow(c,dp)%p
    mq=pow(c,dq)%q

    gcd,yp,yq=ext_euc(p,q)

    m=(mp*yq*q+mq*yp*p)%n
    return m
print(chin_rem(463,547,47,47))
