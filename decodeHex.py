data = "0x436f6e67726174756c6174696f6e73206f6e2064656372797074696e6720616e20525341206d6573736167652120596f757220666c6167206973206d6f64756c61725f61726974686d65746963735f6e6f745f736f5f6261645f61667465725f616c6cL"

print ''.join(chr(int(data[i:i+2],16)) for i in range(2,len(data)-1,2))
