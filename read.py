data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 1000 == 0:  #餘數才列印
			print (len(data))

print ('讀取結束, 總共有', len(data), '筆資料')


sum_1 = 0
for d in data:
	sum_1 = sum_1 + len(d)
	
print ('每筆留言長度為', sum_1 / len(data) )
	





