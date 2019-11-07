

def axn(s):
            alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            news=""
            for i in range(len(s)):
                        if s[i] in alphabets:
                                    var=s[i]
                                    news=news+"x"
                        else:
                                    news=news+s[i]
            s=news
            deriv="(d"+var+"/dx)"
            l=len(s)
            if s=="x":
                        return "1"
            if s[0].isdigit():
                        a=int(s[0])
                        if l==1:
                                    return "0"
                        elif l>2 and s[1]=="x" and s[2]=="^":
                                    b=s[3:len(s)]
                                    b2=int(b)-1
                                    b3=int(s[0])*int(b)
                                    s1=str(b3)+var+"^"+str(b2)
                                    return s1
                        elif s[1]=="x":
                                    return s[0]
            if l>2:
                        if s[0]=="x" and s[1]=="^":
                                    b=s[2:len(s)]
                                    b2=int(b)-1
                                    s1=b+var+"^"+str(b2)
                                    return s1
            
def trigdif(s):
            s1=""
            start=s.find("(")+1
            end=s.find(")")
            var=s[start:end]
            if "^" in var or var[0] in ["1","2","3","4","5","6","7","8","9"]:
                        chain="*"+axn(var)
            elif var.find("sin")!=-1 or var.find("cos")!=-1 or var.find("tan")!=-1 or var.find("cosec")!=-1 or var.find("sec")!=-1 or var.find("cot")!=-1:
                        chain=")"+"*"+trigdif(var+")")
                        s=s[0:s.find("(")+1]+"(x)"
                        
            else:
                        chain=""
                   
            if s.find("sin")!=-1:
                        
                        if s[0].isdigit():
                                    var=s.find("(")+1
                                    s1=s[0]+"cos("+s[var]+")"
                        else:
                                    s1="cos("+var+")"
                        return s1+chain
            if s.find("cos")!=-1:
                        if s[0].isdigit() or s[0]=="-":
                                    var=s.find("(")+1
                                    s1=s[0]+"-sin("+s[var]+")"
                        else:
                                    s1="-sin("+var+")"
                        return s1+chain

            if s.find("tan")!=-1:
                        if s[0].isdigit():
                                    var=s.find("(")+1
                                    s1=s[0]+"sec^2("+s[var]+")"
                        else:
                                    s1="sec^2("+var+")"
                        return s1+chain
            if s.find("cosec")!=-1:
                        if s[0].isdigit():
                                    var=s.find("(")+1
                                    s1=s[0]+"-cosec("+s[var]+")"+"cot("+s[var]+")"
                        else:
                                    s1="-cosec("+var+")"+"cot("+var+")"
                        return s1+chain
            if s.find("sec")!=-1:
                        if s[0].isdigit():
                                    var=s.find("(")+1
                                    s1=s[0]+"sec("+s[var]+")"+"tan("+s[var]+")"
                        else:
                                    s1="sec("+var+")"+"tan("+var+")"
                        return s1+chain
            if s.find("cot")!=-1:
                        if s[0].isdigit():
                                    var=s.find("(")+1
                                    s1=s[0]+"-cosec^2("+s[var]+")"
                        else:
                                    s1="-cosec^2("+var+")"
                        return s1+chain
                                    
def differentiate(y):
            l=y.split('+')
            sum=""
            for i in l:
                        
                        if i.find("sin")!=-1 or i.find("cos")!=-1 or i.find("tan")!=-1 or i.find("cosec")!=-1 or i.find("sec")!=-1 or i.find("cot")!=-1:
                                    sum=sum+trigdif(i)+"+"
                        else:
                                    
                                    sum=sum+axn(i)+"+"
                        
                                    
            return (sum[0:len(sum)-1])

y=input()
differentiate(y)
print(y)


