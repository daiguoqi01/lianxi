
f=open("geci","r",encoding="utf-8")
f2=open("gesi2","w",encoding="utf-8")

for line in f:
    if "在很久很久以前，你离开我 去远空翱翔" in line:
        line=line.replace("在很久很久以前，你离开我 去远空翱翔","在很久很久以前，我是多么希望拥有你 带你去远空翱翔")
        #replace是将久字符替换成为新字符。
        f2.write(line)
    else:
        f2.write(line)
f.close()
f2.close()