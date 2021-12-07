
try:
        fhand = open('mailbox.txt')
except:
        print('File cannot be opened')
        exit()

lines=fhand.readlines()
p=[]
file=open('output.txt', 'w')
for line in lines:
       if 'From:' in line:
           ind=line.find('F ')
           en_ind=line.find('.')
           word=line[ind+1:en_ind+30]
           if word not in p:
              p.append(word)
           p.sort()
for word in p:
   print(word)
   file.write(word)
   file.write('\n')
fhand.close()

