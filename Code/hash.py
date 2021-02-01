
def hash(astring:str, tablesize:int):
    '''
    Hash function realization
    Convert string to a number in hash function
    Input: string
    '''
    sum = 0
    for i in range(len(astring)):
        sum = sum + ord(astring[i])
    return sum % tablesize


if __name__ == "__main__":
    print(hash('hello',11))