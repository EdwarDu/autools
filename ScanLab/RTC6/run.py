from rtc6_sdk import RTC6Man

rtc6_man = RTC6Man()

x, y = 0, 0

while True:
    x = int(input("Goto X:"))
    y = int(input("Goto Y:"))
    rtc6_man.goto_xy(x, y)
