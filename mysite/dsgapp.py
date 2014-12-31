from sys import argv

script, filename = argv

def parse(filename):

    txt = open(filename)
    strs = ""
    strs2 = ""
    flag = False
    flag2 = False
    for i in txt.readlines():
        if "-----" in i:
            flag = not flag
        if flag==True and "-----" not in i:
            strs+=i
        if "$$$$$" in i:
            flag2 = not flag2
        if flag2 == True and "$$$$$" not in i:
            strs2+=i
    dump=open('dump.py', 'w')
    dump.writelines(strs)
    dump.close()
    dump2=open('dump.py')
    dump3=open('dump_list.py','w')
    ret={}
    for j in dump2.readlines():
        z=j
        z2=z.split("=")
        if len(z2) >1:
            z2[1]=z2[1] if  z2[1][-1]!='\n' else z2[1][:-1]
        flag3 = False
        dump3.write(z2[0])
        try:
            float(z2[1])
            isFloat = True
            ret[z2[0]]=float(z2[1])
        except:
            isFloat = False
            ret[z2[0]]=z2[1]

        if isFloat == True:
            dump3.write('=')
            dump3.write(z2[1])
        elif isFloat == False:
            dump3.write('="')
            dump3.write(z2[1])
            dump3.write('"')

        dump3.write('\n')
    dump3.close()
    #a=__import__('dump_list')
    #a.__dict__['content']=strs2
    ret['content']=strs2
    return ret
print parse( filename)['content']
