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
    '''
    This function will convert s1,s2 to list and then sort, 
    find out whether the sorted list are exactly the same.
    Sorting method dominant the algo.
    This is O(n^2) or O(nlogn) algorithm depending on sorting method.
    '''
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

def anagram3(s1,s2):
    '''
    This function will count the frequency of 26 characters in s1,s2 using a 26 characters list. 
    find out whether the counts are exactly the same.
    This is O(n) algorithm depending on sorting method.
    '''
    count1 = [0]*26
    count2 = [0]*26
    stillOK = True
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        count1[pos] = count1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        count2[pos] = count2[pos] + 1
    for i in range(len(count1)):
        if count1[i] != count2[i]:
            stillOK = False
    return stillOK

def anagram4(s1,s2):
    '''
    This function will count the frequency of 26 characters in s1,s2 using dictionary. 
    find out whether the counts are exactly the same.
    This is O(n) algorithm depending on sorting method.
    '''
    dict1 = dict()
    dict2 = dict()
    stillOK = True
    for c in s1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1[c] += 1
    for c in s2:
        if c not in dict2:
            dict2[c] = 1
        else:
            dict2[c] += 1
    return dict1 == dict2
            

if __name__ == "__main__":
    print(anagram1('python','typhon'))
    print(anagram1('hhhhhh','typhon'))
    print(anagram2('python','typhon'))
    print(anagram2('hhhhhh','typhon'))
    print(anagram3('python','typhon'))
    print(anagram3('hhhhhh','typhon'))
    print(anagram4('python','typhon'))
    print(anagram4('hhhhhh','typhon'))
    

