# to read file in the current directory
# file =open('File/file.txt')
# reading whole file 

# data= file.read() 
# print(data)

# reading file line by line
# lines = file.readlines()
# print(lines,type(lines))

# reading file one line
# line1 = file.readline()
# print(line1,type(line1))

# line2 = file.readline()
# print(line2,type(line2))

# append data at the end of file

file =open('File/file.txt','a')  # 'a' mode for appending
file.write('\nShahmir  added new line to the file.')
file.close()
