key = (71+76+85+71)<<8
buf = [0x12f78, 0x12f30, 0x12f72, 0x12f5f, 0x12f61, 0x12f6e, 0x12f64, 0x12f5f, 0x12f6c, 0x12f30, 0x12f67, 0x12f31, 0x12f63, 0x12f40, 0x12f6c, 0x12f5f, 0x12f73, 0x12f68, 0x12f31, 0x12f66, 0x12f74, 0x12f5f, 0x12f65, 0x12f40, 0x12f73, 0x12f79, 0x12f5f, 0x12f72, 0x12f31, 0x12f67, 0x12f68, 0x12f38, 0x12f3f, 0x12f3f]
flag = ""
for i in buf:
	flag += chr(i^key)
print flag