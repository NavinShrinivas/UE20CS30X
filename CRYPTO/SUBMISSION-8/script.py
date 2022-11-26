payload = bytearray("******:myname=pes2ug20cs237&uid=1002&lstcmd=1", "utf8")
length_field = (len(payload) * 8).to_bytes(8, "big")
padding = b"\x80" + b"\x00" * (64 - len(payload) - 1 - 8) + length_field
print("".join("\\x{:02x}".format(x) for x in padding))
# for url-encoding
print("".join("%{:02x}".format(x) for x in padding))
