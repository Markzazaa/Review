data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:  #餘數才列印
			print (len(data))
			

print ('讀取結束, 總共有', len(data), '筆資料')


sum_2 = 0
for k in data:
	sum_2 = sum_2 + len(k)

print ('讀取結束, 平均留言長度為:', sum_2 / len(data))
 


new = []
for z in data:
	if len(z) < 300:
		new.append(z)

print ('小於300字的留言有', len(new), '筆')