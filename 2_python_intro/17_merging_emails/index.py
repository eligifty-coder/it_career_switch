with open("hello.txt",'w') as file:
   file.write("Hey there!!")

x = open("hello.txt",'r')
print(x.read())
x.close()

with open('names.txt','r') as n_file:
   with open('message.txt','r') as m_file:
      body = m_file.read()
      for name in n_file:
         mail = "hello " + name + body
         with open(name.strip()+'.txt', 'w') as messageFile:
            messageFile.write(mail)