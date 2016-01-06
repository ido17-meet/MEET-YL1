s  = input("i know the answer => ")
y=len(s)-1
pal=True
for i in range(len(s)):
	if s[i]!=s[y]:
		pal=False

	y-=1

print(pal)