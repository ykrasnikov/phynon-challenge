# import os / re library
import os
import re
# define path , open file , read to para
file_path=os.path.join("raw_data","paragraph_3.txt")
with open(file_path) as text_file:
    para = text_file.read().replace('\n',' ')
print(para) # debug print
character_count= len(para)
print(character_count) # debug print
letter_count=len(re.sub(r"\W", "", para, flags=re.I))
print(letter_count) # debug print


#word count
word_count=len(para.split()) 

#sentence/letter/word count
sentence_count=len(re.split("(?<=[.!?]) +", para))
letter_word="{:.1f}".format(letter_count/word_count)
word_sentence="{:.1f}".format(word_count/sentence_count)

# Print Analysis - create list of strings with print content
prn_str="Paragraph Analysis \n"+"-"*40+"\n"
prn_str+=f"Approximate Word Count: {word_count}\n"
prn_str+=f"Approximate Sentence Count: {sentence_count}\n"
prn_str+=f"Average Letter Count: {letter_word}\n"
prn_str+=f"Average Sentence Length: {word_sentence}\n"

print(prn_str)
# file path to write
file_path2 = os.path.join('raw_data', 'Paragraph_results.text')

# Open File Using to "Write". and write print list
with open(file_path2, 'w') as txt_file:
     txt_file.write(prn_str)
print(f'\n File is created/(written over) at {file_path2}" \n the end')