from rtc6_sdk import RTC6Man

rtc6_man = RTC6Man()
rtc6_man.config_list(-1, 0)
rtc6_man.load_correction_file(None, 1, 2) # load Cor_1to1.ct5 comes with package, use table #1, use 2D only

x, y = 0, 0

while True:
    x = int(input("Goto X:"))
    y = int(input("Goto Y:"))
    rtc6_man.goto_xy(x, y)
