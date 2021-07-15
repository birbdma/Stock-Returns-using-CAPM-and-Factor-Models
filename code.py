import numpy as np

########Excess return
# f = open("PI.csv", "r")
# fr = f.readlines()
# fw = open("exret.csv", "w+")
# for i in range(len(fr)):
#     if i==0:
#         fw.write(fr[0])
#     else:
#         a = fr[i].split(",")
        
#         l = a[0]+","+a[1]+","+a[2]+","+","
#         for j in range(4,41):
#             b = np.log(float(a[j])/float(a[j-1]))*100 - 1.13
#             l = l + str(b) + ","
#         l = l + "\n"

#         fw.write(l)

########Excess return
f1 = open("MVFF.csv", "r")
f2 = open("exret.csv", "r")
f3 = open("PTBV.csv","r")
fr1 = f1.readlines()
fr2 = f2.readlines()
fr3 = f3.readlines()
fw = open("smb.csv", "w+")
matmvff = np.zeros((54,37))
matexret = np.zeros((54,37))
matptbv = np.zeros((54,37))
for i in range(len(fr1)):
    if i==0:
        pass
    else:
        a1 = fr1[i].split(",")
        a2 = fr2[i].split(",")
        a3 = fr3[i].split(",")
        for j in range(37):
            matmvff[i-1,j] = float(a1[j+4])
            matexret[i-1,j] = float(a2[j+4])
            matptbv[i-1,j] = float(a3[j+4])

mat1sort = np.zeros((54,37))
mat2sort = np.zeros((54,37))
mat3sort = np.zeros((54,37))

for i in range(37):
    seq1 = np.argsort(-1*matmvff[:,i])
    seq2 = np.argsort(-1*matptbv[:,i])
    seq3 = np.argsort(-1*matexret[:,i])
    mat1sort[:,i] = matexret[seq1,i]
    mat2sort[:,i] = matexret[seq2,i]
    mat3sort[:,i] = matexret[seq3,i]

bigg = []
smalll = []
smbb = []
hmll = []
momm = []

# print(mat1sort[:9,10])

for i in range(37):
    big = np.sum(mat1sort[:27,i])*(1.0/27)
    small = np.sum(mat1sort[27:,i])*(1.0/27)
    value = np.sum(mat2sort[:18,i])*(1.0/18)
    neutral = np.sum(mat2sort[18:36,i])*(1.0/18)
    growth = np.sum(mat2sort[36:,i])*(1.0/18)
    high = np.sum(mat2sort[:16,i])*(1.0/16)
    low = np.sum(mat2sort[38:,i])*(1.0/16)
    smb = (1/3.0)*(small*value + small*neutral + small*growth - big*value - big*neutral - big*growth)
    hml = (1/2.0)*(small*value - small*growth + big*value - big*growth)
    mom = (1/2.0)*(small*high + big*high - small*low - big*low)
    smalll.append(small)
    bigg.append(big)
    smbb.append(smb)  
    hmll.append(hml)
    momm.append(mom)




for i in range(6):
    if i==0:
        fw.write(fr1[0])
        continue
    a = ",,,,"
    if i==1:
    	for j in range(len(bigg)):
    		a = a+str(bigg[j])+","
    if i==2:
    	for j in range(len(smalll)):
    		a = a+str(smalll[j])+","
    if i==3:
    	for j in range(len(smbb)):
    		a = a+str(smbb[j])+","
    if i==4:
    	for j in range(len(hmll)):
    		a = a+str(hmll[j])+","
    if i==5:
    	for j in range(len(momm)):
    		a = a+str(momm[j])+","

    fw.write(a+"\n")

        






