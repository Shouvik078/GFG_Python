
#vowel Count in string
# [] list with duplicate

def countVowels(self,s):
    vowel={"a","e","i","o","u"}
    res=[x for x in s if x in vowel]
    return len(res)


# distinct vowel Count in string
# {} set no duplicate

def countVowels(self,s):
        vowel={"a","e","i","o","u"}
        res={x for x in s if x in vowel}
        return len(res)