def l_c_m(*nums):
	ans=1

	for num in nums:
		smaller=min(ans,num)
		hcf=1
		for i in range(1,smaller+1):
			if (num%i==0) and (ans%i==0) and (hcf<i):
				hcf=i
		ans=(ans*num)/hcf
	return ans

print(l_c_m(12,10,5,12,3,15,25))
