'''
Author: Ivy Xue
Time: 11/23/2020
This file solves Anagram Problem.
Description: Anagram is a word or phrase made by transposing the letters of another word or phrase.
Input Parameter: two words s1, s2 with the same length and all the letters are lower case.
The function will return whether the two words are anagram.
Return: True or False
'''

def anagram1(s1,s2):
    '''
    This function will literate through s1, find out whether each charater in s1 can be found correspondingly in s2.
    There are nested loops in this algo. 
    This is O(n^2) algorithm.
    '''
    pos1 = 0
    list2 = list(s2)
    stillOK = True
    while pos1 < len(s1) and stillOK :
        pos2 = 0
        found = False
        while pos2 < len(list2) and not found:  
            if s1[pos1] == list2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found :
            list2[pos2] = None
        else :
            stillOK = False
        pos1 = pos1 + 1
    return stillOK


def anagram2(s1,s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    stillOK = True
    for i in range(len(s1)):
        if list1[i] != list2[i]:
            stillOK = False
            break
    return stillOK

if __name__ == "__main__":
    print(anagram2('hhhhhh','typhon'))
    

