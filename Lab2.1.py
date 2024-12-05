S1 = "Maha Bharat"
s1_modified = "".join([char.upper() if char.islower() else char.lower() for char in S1])
bharat = S1[5:]
bharat_repeated = bharat * 3
mera_bharat = S1.replace("Maha", "Mera")
mera_bharat_mahan = mera_bharat + " Mahan"

print(s1_modified)
print(bharat)
print(bharat_repeated)
print(mera_bharat)
print(mera_bharat_mahan)





