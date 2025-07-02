 

def replace_word_in_file(file_path, old_word, new_word):
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = content.replace(old_word, new_word)
    
    with open(file_path, 'w') as file:
        file.write(content)
        
replace_word_in_file('File/file.txt','#####',"horse")