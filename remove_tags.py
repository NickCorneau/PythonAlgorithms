# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(s):
    arr = []
    open_tag = s.find('<')
    close_tag = s.find('>')
    
    if open_tag != 0:
        word = s[:open_tag].split()
        for i in word:
            arr.append(i)

    if open_tag == -1:
        return s.split()            
    
    while (open_tag != -1):                
        word = s[close_tag+1:s.find('<', open_tag+1)]
        if s.find('<', open_tag+1) == -1:
            word = s[close_tag+1:]
        if (word != ''):
            if '\n' in word:
                word = word[:word.find('\n')]
            word = word.split()
            for i in word:
                arr.append(i)               
        open_tag = s.find('<', open_tag+1)
        close_tag = s.find('>', open_tag)
    return arr

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("<br />This line starts with a tag")
#>>> ['This', 'is', 'plain', 'text.']