import mindwave,time

port="COM4"
mid="1425"
rate=0.001953125

headset = mindwave.Headset(port,mid)

headset.connect()
print "Connecting"

while headset.status != "connected":
	time.sleep(0.5)
	if headset.status == "standby":
		headset.connect()
		print "Retrying connect..."
print "Connected."

While True:
	print headset.raw_value
	time.sleep(rate)