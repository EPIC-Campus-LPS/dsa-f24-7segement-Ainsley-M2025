import tm1637
import time

tm = tm1637.TM1637(clk=17, dio=18)
clear = [0, 0, 0, 0]

tm.write(clear)
time.sleep(1)
s ="Hello Name"
tm.scroll(s, delay=250)
time.sleep(2)
