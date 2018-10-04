def Sha1_Brute_With_Names(reqdsha1,filename):
	import hashlib
	f=open(filename,'r')
	s=f.readlines()
	for i in range(len(s)):
		s[i]=s[i].strip()
		s[i]=s[i].title()
		#for changing the first letter to Uppercase
		eachpwd = s[i] + " Snow"
		sha_1 = hashlib.sha1()
		sha_1.update(eachpwd)
		finalhash = sha_1.hexdigest()
		if(finalhash==reqdsha1):
			print ("Name: " + eachpwd)

Sha1_Brute_With_Names("SHAHERE", "file.txt")