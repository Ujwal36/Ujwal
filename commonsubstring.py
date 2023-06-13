def commonsubstring(string):
    common = string[0]
    for i in range(1,len(string)):
        if common.find(string[i]) == 0:
            common = string[i]
            
        elif common.find(string[i]) == -1:
            
            if common != "" and common[0] == string[i][0]:
                for j in range(len(string[i])):
                    print("string", string[i][:j+1])
                    if common.find(string[i][:j+1]) == -1:
                        common = string[i][:j]
                        print("inside:", common)
                        break
                    else: print(common)
            else:
                common = ""
        
        else:
            common = ""
    print(common)       



string = ["aa","ab"]
commonsubstring(string)