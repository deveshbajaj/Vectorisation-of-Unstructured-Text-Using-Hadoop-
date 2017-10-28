from collections import Counter
import re
cnt = Counter()
	
dev= "devesh is is a good boy040"
st = re.findall(r'\w+',dev)

for i in st:
	cnt[i] +=1

print(cnt)