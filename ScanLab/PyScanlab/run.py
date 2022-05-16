from pyscanlab import RTC6Helper

rtc6_h = RTC6Helper(True)

rtc6_h.load_program_file()
rtc6_h.load_correction_file(None, 1, 2) # load Cor_1to1.ct5 comes with package, use table #1, use 2D only

x, y = 0, 0

while True:
    x = int(input("Goto X:"))
    y = int(input("Goto Y:"))
    rtc6_h.goto_xy(x, y)
