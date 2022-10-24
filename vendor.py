def csvCompare(mac):
	with open(filename) as filp:
		reader = DictReader(filp)

		for row in reader:
			if (row['vendor_mac'] == mac):
				return dict(row)
