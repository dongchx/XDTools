from docx import Document
import sys

def e_trans_to_c(string):
    E_pun = u',.!?[]()<>"\''
    C_pun = u'，。！？【】（）《》“‘'
    table= {ord(f):ord(t) for f,t in zip(E_pun,C_pun)}
    return string.translate(table)

fileName = "default"
if len(sys.argv) >= 2:
    fileName = sys.argv[1]
else:
    print("error: fileName required")

doc = Document(fileName)

print('###### 输出' + fileName + '文章内容')

for p in doc.paragraphs:
    p.text = e_trans_to_c(p.text)
    print(p.text)

doc.save("fix_punctuation_" + fileName)

print('done!')
