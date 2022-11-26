import hmac
import hashlib
key="123456"
message="lstcmd=1&uid=1001&myname=pes2ug20cs237"
mac = hmac.new(bytearray(key.encode("utf-8")),
msg=message.encode("utf-8", "surrogateescape"),
digestmod=hashlib.sha256).hexdigest()
print(mac)
