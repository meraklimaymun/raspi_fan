import RPi.GPIO as GPIO
import time
import os
# Islemci sicakligi bilgisini aliyoruz.
def getCPUtemp(): #getCPUtemp degiskenine yazdiriyoruz.
    cTemp = os.popen('vcgencmd measure_temp').readline()
    return float(cTemp.replace("temp=","").replace("'C\n",""))

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setwarnings(False)
p=GPIO.PWM(2,100)

while True:
    time.sleep(5) # Islemciyi cok mesgul etmemek icin 5 saniye bekleme koyuyoruz.
    CPU_temp = getCPUtemp()
    if CPU_temp > 90.0: #Eger islemci sicakligi 90 derece ustundeyse...
         p.start(100)   #Fani tam devir dondur..
    elif (CPU_temp < 89.0 and CPU_temp >80.0): #Eger islemci 89 ile 80 derece arasindaysa
	 p.start(35) #Fani %35 devirle dondur gibi.....
    elif (CPU_temp < 79.0 and CPU_temp > 70.0):
	 p.start(30)
    elif (CPU_temp < 69.0 and CPU_temp > 60.0):
	 p.start(25)
    elif (CPU_temp < 59.0 and CPU_temp > 50.0):
	 p.start(20)
    elif (CPU_temp < 49.0 and CPU_temp > 40.0):
         p.start(15)
    elif (CPU_temp < 39.0 and CPU_temp > 35.0):
	 p.start(10)
    elif (CPU_temp < 34.0 and CPU_temp > 0.0): #35 derece altinda ise fani kapat...
         p.start(0)

GPIO.cleanup()
