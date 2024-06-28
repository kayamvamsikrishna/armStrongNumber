def isArmStrongNum(a):
    dummy=a
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**len(str(a))
    if summ==a:
        return True
    else:
        return False
if __name__=='__main__':
    ll=int(input('Enter lower limit='))
    ul=int(input('Enter upper limit='))
    for a in range(ll,ul+1):
        if isArmStrongNum(a):
            print(a,' ',end='')