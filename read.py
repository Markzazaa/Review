data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:  #餘數才列印
			print (len(data))


