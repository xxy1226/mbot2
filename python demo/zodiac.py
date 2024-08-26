from termcolor import *
constellation="白羊金牛双子巨蟹狮子处女天枰天蝎射手摩羯水瓶双鱼"
for i in range(12):
    pos=2*i
    if i%3==0 :
        print()
    a=colored("{:^5}".format(chr(9800+i)), "green", "on_cyan")
    b = "{:<2}".format(constellation[pos:pos + 2] + "座")
    print(a,b,end=" ")
print()

print(chr(9800))
