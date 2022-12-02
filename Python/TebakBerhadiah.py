kunci = 5
menang = 0

print("Paket 1 = 2x Percobaan\nPaket 2 = 4x Perobaan\nPaket 3 = 6x Percobaan\nPaket 4 = 8x Percobaan")

while menang == 0:
	paket = int(input("\npilih paket = "))
	if 1 <= paket <= 4:
		for i in range (0,paket*2):
			tebak = int(input("Masukkan Angka  = "))
			if tebak == kunci:
				print("\n🔥SELAMAT ANDA MENANG🔥")
				menang = 1
				break
			else:
				print("coba lagi 😭")
				continue
	else:
		print("masukkan angka 1/2/3/4")
		continue
	if menang == 0:
		lagi = input("beli paket lagi? (y/n)\n")
		if lagi == "n":
			break
