import argparse,os
def get_args():
    parser = argparse.ArgumentParser() 
    parser.add_argument('workdir')
    parser.add_argument('lng1')
    parser.add_argument('lng2')
    args = parser.parse_args()
    return args

def read_txt(file, remove_line_break=True, ignore_extention=False):
    if file[-4:]!=".txt" and not ignore_extention:
        raise ValueError("'file' should be a text file.")

    with open(file,encoding="utf-16") as f:
        if remove_line_break:
            lines = f.read().splitlines()
        else:
            lines = f.readlines()
    #if remove_line_break:
    #   return ['a','b','c',...]
    #else:
    #   return ['a\n','b\n','c\n',...]
    return lines

def write_txt(file, lines, insert_line_break=True, ignore_extention=False):
    if file[-4:]!=".txt" and not ignore_extention:
        raise ValueError("'file' should be a text file.")

    with open(file, "w", encoding="utf-16") as f:
        if insert_line_break:
            f.write("\n".join(lines)) 
        else:
            f.writelines(lines)

def get_filelist(dir, extention=None, root=""):
    l=[]
    for f in os.listdir(dir):
        file_path=os.path.join(dir,f)
        if os.path.isdir(file_path):
            #l=l+get_filelist(file_path, extention=extention, root=os.path.join(root, f))
            continue
        else:
            if (extention is not None) and (f.split(".")[-1]!=extention):
                continue
            l.append(os.path.join(root,f))
    return sorted(l)

def extract_text(txt):
    if txt[0]=="<string" or txt[0][:5]=="<TIME" or txt[0][:2]=="<0" or txt[0][:5]=="<ICON":
        txt=extract_text(txt[1:])
    return txt

def mix_txt(lng1,lng2):
    lng1s=lng1.split("<PAGE>")
    lng2s=lng2.split("<PAGE>")
    new_txt=[lng1s[i]+"<lf>"*int(not lng2s[i][:4]=="<lf>")+lng2s[i] for i in range(len(lng1s))]
    return "<PAGE>".join(new_txt)
    
if __name__=="__main__":
    args=get_args()
    workdir=args.workdir
    lng1=args.lng1
    lng2=args.lng2

    file_list=get_filelist(workdir, extention="17", root="workdir")
    for f in file_list:
        l1txt=read_txt(f+"."+lng1+".txt")
        l2txt=read_txt(f+"."+lng2+".txt")
        newtxt=[]
        for i in range(len(l1txt)):
            txt=l1txt[i]
            if txt=="<string>" or txt=="" or txt[0:14]=="<string><COLOR":
                newtxt.append(txt)
            else:
                l2=">".join(extract_text(l2txt[i].split(">")))
                if l2=="":
                    newtxt.append(txt)
                    continue
                l1=">".join(extract_text(l1txt[i].split(">")))
                head=txt.replace(l1,"")
                if "<PAGE>" in l1:
                    newtxt.append(head+mix_txt(l1,l2))
                else:
                    newtxt.append(head+l1+"<lf>"+l2)
        write_txt(f+".txt", newtxt)

