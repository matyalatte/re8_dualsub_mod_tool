import argparse,os
def get_args():
    parser = argparse.ArgumentParser() 
    parser.add_argument('workdir')
    parser.add_argument('lng1')
    parser.add_argument('lng2')
    parser.add_argument('--verbose', action='store_true')
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
    if txt[0]=="<string" or txt[0][:5]=="<TIME" or txt[0][:2]=="<0":
        txt=extract_text(txt[1:])
    return txt

def mix_txt(lng1,lng2):
    lng1s=lng1.split("<PAGE>")
    lng2s=lng2.split("<PAGE>")
    new_txt=[lng1s[i]+"<lf>"*int(not lng2s[i][:4]=="<lf>")+lng2s[i] for i in range(len(lng1s))]
    return "<PAGE>".join(new_txt)
    
def mix_txt2(lng1,lng2, verbose=False):
    lng1s=lng1.split("<ICON")
    lng2s=lng2.split("<ICON")
    if verbose:
        print("lng1:", lng1s)
        print("lng2:", lng2s)
    new_txt=[]
    for i in range(len(lng1s)):

        if lng1s[i]==lng2s[i]:
            new_txt.append(lng1s[i])
            continue
        lng1_=lng1s[i].split(">")
        lng2_=lng2s[i].split(">")
        new_txt.append(lng1_[0]+">"+lng1_[1]+"/"+lng2_[1])
    return "<ICON".join(new_txt)

def mix_txt3(l1,l2):
    if l1[:4]=="<REF" and l1.split(">")[1]=="":
        return l1
    l1_l=l1.lower()
    l2_l=l2.lower()
    if l2_l in l1_l or (l2_l==l1_l+"s") or\
      (l2_l==l1_l+"es") or (l2_l==l1_l[:-1]+"ies") or (l2_l=="the "+l1_l)\
   or ("concept" in l2_l and "art" in l1_l and not ("<lf>" in l1_l)):
        return l2
    elif l1_l.replace(' ', '') == l2_l:
        return l1
    else:
        return l1+"<lf>"+l2

if __name__=="__main__":
    args=get_args()
    workdir=args.workdir
    lng1=args.lng1
    lng2=args.lng2
    verbose=args.verbose

    file_list=get_filelist(workdir, extention="17", root=workdir)
    for f in file_list:
        if verbose:
            print(f)
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
                if verbose:
                    print("i:{}".format(i))
                    print("  l1:{}".format(l1))
                    print("  l2:{}".format(l2))
                if "<PAGE>" in l1:
                    newtxt.append(head+mix_txt(l1,l2))
                elif (l1[:5]=="<ICON") and not ("<lf>" in l1):
                    newtxt.append(head+mix_txt2(l1,l2, verbose=verbose))
                else:
                    newtxt.append(head+mix_txt3(l1,l2))
                if verbose:
                    print("  txt:{}".format(newtxt[-1]))
        write_txt(f+".txt", newtxt)

