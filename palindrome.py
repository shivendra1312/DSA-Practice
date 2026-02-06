

def palindrome(word,left,right):
    if left>=right:
        return True
    if word[left]!=word[right]:
        return False
    else:
        return palindrome(word,left+1,right-1)


        
word = input("enter a string: ")

if palindrome(word, 0, len(word) - 1):
    print("palindrome")
else:
    print("not palindrome")

    
