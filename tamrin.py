import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
try:
    x1=int(input("عدد اول رو وارد کن:"))
    x2=int(input("عدد اول رو وارد کن:"))
    x3=int(input("عدد اول رو وارد کن:"))
    result=[x1,x2,x3]
    result.sort()
    print(result)
except ValueError:
    print("داده نامعتبر می باشد لطفا عدد واردکنید")