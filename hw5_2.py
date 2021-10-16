def check_str(s_temp, s_to_check, f_at_cnt):  
  if len(s_to_check)<len(s_temp):
    return False
  for i in range(f_at_cnt,len(s_temp),1):
    if s_temp[i]=='@':
      continue
    if s_temp[i]!=s_to_check[i]:
      return False

  return True



def find_str_temp(s, temp): 
  l_temp = temp.split()
  ind = 0
  first_at_count = 0 
    
  for i in range(len(l_temp[0])):   
    if l_temp[0][i]=='@':
      first_at_count+=1
    else:
      break

  f=temp.split('@')[first_at_count]

  if len(temp)==first_at_count: 
      return 0 if len(s)>= len(temp) else -1

  while True:   
    ind = s.find(f, ind)    
    if ind==-1:
      return ind
    
    if check_str(temp,s[ind - first_at_count:ind+len(temp)],first_at_count):
      return ind - first_at_count

    ind+=1
    
    
s=input()
temp=input()
print(find_str_temp(s,temp))

