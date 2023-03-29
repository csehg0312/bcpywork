

def binaris_kereses(listaban_keresni, query):
    bal, jobb = 0, len(listaban_keresni) - 1
    matches = []

    while bal <= jobb:
        kozep = (bal + jobb) // 2
        if listaban_keresni[kozep].lower().rfind(query) != -1:
            #print(listaban_keresni[kozep].lower())
            #print(listaban_keresni[kozep].rfind(query))
            # Found a match
            matches.append(listaban_keresni[kozep])
            
            # Check if there are more matches to the bal
            for i in range(kozep-1, -1, -1):
                if listaban_keresni[i].lower().rfind(query) != -1:
                    #print(listaban_keresni[i].lower())
                    #print(listaban_keresni[i].rfind(query))
                    matches.append(listaban_keresni[i])
                else:
                    continue
            
            # Check if there are more matches to the jobb
            for i in range(kozep+1, len(listaban_keresni)):
                if listaban_keresni[i].lower().rfind(query) != -1:
                    #print(listaban_keresni[i].lower())
                    #print(listaban_keresni[i].rfind(query))
                    matches.append(listaban_keresni[i])
                else:
                    continue
            
            return matches

        elif query < listaban_keresni[kozep]:
            jobb = kozep - 1
        else:
            bal = kozep + 1
    
    return matches

def binaris_atvitel(listaban_keresni, query) -> list:
    talalat:list = binaris_kereses(listaban_keresni, query)
    return talalat



