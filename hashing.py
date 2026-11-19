## Integer Hashing

# method - 1 Using List when the length limit of the hashmap is know use this
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

        # 1<=n<=10

hashlist = [0] * 11

for num in n:
    hashlist[num]+=1

print(hashlist)
# for val in m:
#     if val in hashlist:
#         print(hashlist[val])
#     else:
#          print("0")

# OR
for val in n:
    if val<1 or val>10:
        print("0")
    else:
         print(hashlist[val])

# method - 2 using a dictionary when the lenght limit of the hashmap is not known

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

mydict = {}

for i in range(len(n)):
    if n[i] in mydict:
        mydict[n[i]]+=1
    else:
         mydict[n[i]]=1

print(mydict)

for val in m:
    if val in n:
        print(mydict[val])
    else:
         print("0")


## Character Hashing

s = "azyxyyzaaaa"
q = ['d','a','y','x']

l = [0]*26

for ch in s:
    ascii_val = ord(ch)                 
    #ord() function takes a single character and returns its integer Unicode code point. For standard English letters, numbers, and symbols, this integer matches the character's ASCII value
    # print(ascii_val)
    idx = ascii_val - 97
    l[idx]+=1
print(l)

for ch in q:
        ascii_val = ord(ch)
        idx = ascii_val - 97
        print(l[idx])
