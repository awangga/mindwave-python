import mindwave,time
import os

port="/dev/null"
mid="1425"
rate=0.001953125
namafile="hasilnya.csv"
runfile="run"

open(runfile, 'a').close()

headset = mindwave.Headset(port,mid)

headset.connect()
print("Connecting")

while headset.status != "connected":
	time.sleep(0.5)
	if headset.status == "standby":
		headset.connect()
		print("Retrying connect...")
print("Connected.")

f=open(namafile,'a+')

while True:
    if os.path.exists(runfile)!=True:
        f.close()
        break
    try:
        while True:
            f.write(headset.raw_value+',0\n')
            time.sleep(rate)
            if os.path.exists(runfile)!=True:
                f.close()
                break
    except KeyboardInterrupt:
        f.write(headset.raw_value+',1\n')
        if os.path.exists(runfile)!=True:
            f.close()
            break
        continue
	
