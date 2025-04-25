def mergeAlternately(word1, word2):
    ch = list(word1)
    ch2 = list(word2)
    ch3 = []
    
    print("______________________________")
    if len(ch) > len(ch2):
        diff = len(ch) - len(ch2)
        s = ch[diff:]
        ch = ch[:diff]
        for i in range(len(ch)):
            if i <= len(ch) - 1:
                ch3.append(ch[i])
            if i <= len(ch2) - 1:
                ch3.append(ch2[i])
        ch3.extend(s)
        print("ch1 is big")
        print(ch3)
    elif len(ch2) > len(ch):
        
        diff = len(ch2) - len(ch)
        s = ch2[diff:]
        ch2 = ch2[:diff]
        for i in range(len(ch2)):
            if i <= len(ch) - 1:
                ch3.append(ch[i])
            if i <= len(ch2) - 1:
                ch3.append(ch2[i])
            
        ch3.extend(s)
        print("ch1 is small")
    else:
        for i in range(len(ch)):
            ch3.append(ch[i])
            ch3.append(ch2[i])
              
            
    print("".join(ch), "".join(ch2), "".join(ch3))
    

         def mergeAlternately(word1, word2):
    result = []
    i = 0
    min_len = min(len(word1), len(word2))

    # Alternate characters from both
    while i < min_len:
        result.append(word1[i])
        result.append(word2[i])
        i += 1

    # Append remaining characters
    result.append(word1[i:])
    result.append(word2[i:])

    return ''.join(result)
   
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i, j = 0, 0
        merged = []
        len1 , len2 = len(word1), len(word2)
        while i < len1 and j < len2 :
            merged.append(word1[i])
            merged.append(word2[j])
            i=i+1 
            j=j+1 

        merged.extend(word1[i:])
        merged.extend(word2[j:])

        return "".join(merged)           
    
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = max(len(word1), len(word2))
        res = ''
        for i in range(n):
            if i <len(word1):
                res += word1[i]
            if i <len(word2):
                res += word2[i]
        return res  
    
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""

        i = 0
        length = len(word1) + len(word2)
        list1 = list(word1)
        list2 = list(word2)
        for i in range(length):
            if i < len(list1):
                result = result + list1[i]
            if i < len(list2):
                result = result + list2[i]
            i += 1   
    
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # l1 = len(word1)
        # l2 = len(word2)
        # s = ""
        # i = j = 0
        # while i < l1 and j < l2:
        #     s += word1[i] + word2[j]
        #     i += 1
        #     j += 1
        # if l1 < l2:
        #     s += word2[j:]
        # else:
        #     s += word1[i:]
        # return s
        return ''.join(a+b for a, b in zip(word1, word2)) + word1[len(word2):] + word2[len(word1):]   
    
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lenw1 = len(word1)
        lenw2 = len(word2)
        maxlen = max(lenw1, lenw2)
        minlen = min(lenw1, lenw2)
        word3 = ""

        for i in range(maxlen):
            if i + 1 <= minlen:
                word3 += word1[i]
                word3 += word2[i]
            elif lenw1 == maxlen:
                word3 += word1[i]
            else:
                word3 += word2[i]
        return word3    
    
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        min_word_len = len(word1) if len(word1) < len(word2) else len(word2)
        print(min_word_len)

        final_word=""
        for i in range(min_word_len):
            final_word = final_word+word1[i]+word2[i]
        return final_word+word1[min_word_len:]+word2[min_word_len:]    
    
def mergeAlternately( word1, word2):
        new = ""
        k = 0
        a = (word1)
        b = (word2)
        if len(a) > len(b):
            for i in range(len(b)):
                new += a[i]+b[i]
                k += 1
                print(k)
            new += a[k:]
        else:
            for i in range(len(a)):
                new += a[i]+b[i]
                k += 1
                print(k)
            new += b[k:]
            
def mergeAlternately( word1, word2):
        i, j = 0, 0
        result = []

        # Merge characters from both words alternately
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append any remaining characters from word1 or word2
        result.append(word1[i:])
        result.append(word2[j:])
        
        # Join the result list into a string and return
        return ''.join(result)            
            
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = []
        i, j = 0,0
        len1, len2 = len(word1), len(word2)

        while i< len1 and j< len2:
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1

        if i < len1:
            result.append(word1[i:])
        if j < len2:
            result.append(word2[j:])

        return ''.join(result)
    
    
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a=""
        extra = ""
        l1,l2 = len(word1),len(word2)
        if(l1 > l2):
            extra = word1[l2:]
            word1[:l2]
        elif(l1<l2):
            extra = word2[l1:]
            word2[:l1]
        for i in range(0,min(l1,l2)):
            a = a + word1[i]
            a = a + word2[i]
        a = a+extra
        return a        
            
            
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        p1 = 0
        p2 = 0
        while p1 < len(word1) and p2 < len(word2):
            if p1 <= p2:
                output += word1[p1]
                p1 += 1
            else: 
                output += word2[p2]
                p2 += 1
        if p2 < len(word2):
            output += word2[p2:]
        if p1 < len(word1):
            output += word1[p1:]
        return output           
            
def mergeAlternately( word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """


        merged = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[j])
            i = i + 1
            j = j + 1
        merged.extend(word1[i:])
        merged.extend(word2[j:])
        return ''.join(merged)            
            
            
            
            
            
            
            
            
            
            
            
            
                
s = "abc"
s1 = "pqr"
    
mergeAlternately(s, s1)


s = "abc"
s1 = "pqrstuv"
    
mergeAlternately(s, s1)

s = "abcefg"
s1 = "pqr"
    
mergeAlternately(s, s1)

s = "cdf"
s1 = "a"
    
mergeAlternately(s, s1)

s = "f"
s1 = "beebaeca"
    
mergeAlternately(s, s1)

s = "cf"
s1 = "eee"
    
mergeAlternately(s, s1)