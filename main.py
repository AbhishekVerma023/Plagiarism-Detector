import re
from kmp import KMPSearch

root_file=input("Enter The Name of root file ")
plagiarised_file=input("Enter The Name of plagiarised file ")
  
Text = open(root_file,"r")
text = Text.read()

pattern_file = open(plagiarised_file,"r").read()
sentences = re.split(r'[\.\?!\r\n]', pattern_file)
counter_matched = 0
counter_total = 0
p=0
for pattern in sentences:
  pattern = pattern.strip()

  if len(pattern) > 0:
    counter_total +=1
    counter_matched += KMPSearch(pattern, text,p)
          
print ("Match percentage = %s%%" % (counter_matched*100/counter_total))

if(counter_matched*100/counter_total) >= 70 :
  print ("The input file appears to be plagiarised. %s%% of its content matches with the file %s." % ((counter_matched*100/counter_total), root_file))  
