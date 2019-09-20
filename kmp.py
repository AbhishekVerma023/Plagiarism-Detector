from lps import computeLPSArray

def KMPSearch(pat, text, p):

    M = len(pat)
    N = len(text)
    lps = [0]*M
    j = 0 
    computeLPSArray(pat, M, lps)
 
    i = 0 
    while i < N:
        if pat[j].lower() == text[i].lower():
            i += 1
            j += 1
 
        if j == M:
            p +=1
            j = lps[j-1]
            break

        elif i < N and pat[j].lower() != text[i].lower():
            if j != 0:
                j = lps[j-1]
            else:
                i += 1      
    return p
 
