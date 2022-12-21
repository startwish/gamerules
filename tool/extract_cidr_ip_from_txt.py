# importing the module
import re
print('IP EXTRACTOR 1.0 BY Startwish')

filename='text.txt'
# opening and reading the file
with open(filename) as fh:
   fstring = fh.readlines()
 
# declaring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{2})')

# displaying the extracted IP addresses
for index, line in enumerate(fstring):
    result = pattern.findall(line)
    for each in result:
        print(each)
        f = open("ipextracted.txt", "a")
        f.write(each+"\n")
        f.close()