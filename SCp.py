f = open("new.ass",'r',encoding = 'utf-8')
fnew = open("new_SC.ass",'w',encoding = 'utf-8')
for line in f:
    if "\pos(960,490)" in line:
        line = line.replace("\pos(960,490)","\pos(960,1)")
    if "\pos(960,438)" in line:
        line = line.replace("\pos(960,438)","\pos(960,53)")
    if "\pos(960,386)" in line:
        line = line.replace("\pos(960,386)","\pos(960,105)")
    if "\pos(960,334)" in line:
        line = line.replace("\pos(960,334)","\pos(960,157)")
    fnew.write(line)

f.close()
fnew.close()
