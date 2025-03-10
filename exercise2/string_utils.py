# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    L=[]
    for i in s: 
        L.append(i)
    return L[::-1]
    # TODO: Implement this function
    pass


def count_vowels(s: str) -> int:
    L= ['a','e','i','o','u','A','E','I','O','U']
    k=0
    for i in s :
        if i in L :
            k+=1
    return k
   
    # TODO: Implement this function
    pass


def is_palindrome(s: str) -> bool:
    j = len(s)
    n= len(s)
    if j%2 == 0 :
        A1 = s[:n/2:]
        A2 = s[n/2::]

    else :
        A1 = s[:n//2:]
        A2 = s[n//2+1::]
    
    if A1 == A2[::-1] : 
        return True
    return False
    
    # TODO: Implement this function
    pass


def capitalize_words(s: str) -> str:
    mots = s.split()
    for i in mots : 
        k = i[0].upper()+i[1::]
        k=i
        S = ' '.join(mots)
        return S
        
    # TODO: Implement this function
    pass