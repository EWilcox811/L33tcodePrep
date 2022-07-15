def rotate(nums : list, k : int)->None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        print(f'k={k}\n')
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
        print(nums)

nums = [1,2,3,4,5,6,7,8]
rotate(nums,3)

# Move the zeroes in an integer array to the end of the array in place
def moveZeroes(nums:list)->None:
    previous, current = 0, 1

    while previous < len(nums) and current < len(nums):
        if nums[previous] == 0 and nums[current]!=0:
            nums[previous], nums[current] = nums[current],nums[previous]
            previous += 1
        elif nums[previous]!=0:
            previous+=1
        current+=1
nums = [0,1,0,3,12]
moveZeroes(nums)
nums

# find two numbers in an integer array that add up to the target and return the indicies as a base 1
def twoSum(numbers:list, target:int):
    low, high = 0, len(numbers)-1
    while low < high:
        num = numbers[low]+numbers[high]
        if num == target:
            return [low+1, high+1]
        elif num < target:
            low+=1
        else:
            high -=1
    return[-1,-1] # This is returned if solution is not found.
twoSum([2,7,11,15], 9)

# Reverse the letters of each word in a string sentence while preserving the whitespace and word order
def reverseWords(s):
    words = [word for word in s.split()]
    words
    sentence = ''
    i = 0
    while i < len(words):
        if i != len(words)-1:
            sentence += words[i][::-1] + ' '
            i+=1
        else:
            sentence += words[i][::-1]
            i+=1
    return sentence
reverseWords("Let's take LeetCode contest")


# Matching paranthesis
def isValid(s):
    stack = []
    mapping = {')':'(',
               ']':'[',
               '}':'{'}
    for char in s:
        #If the character is a closing bracket
        if char in mapping:
            """
            pop the topmost element from the stack if it isn't empty
            otherwise assign a dummy value of '#' to the top_element variable
            """
            topStack = stack.pop() if stack else '#'
            #If the mapping and the top_element don't match return false
            if mapping[char] != topStack:
                return False
        else:
            #add the opening bracket to the stack
            stack.append(char)
    return not stack
isValid('()')

#Integer to Roman Numerals
def intToRoman(num):
    #create a digit to roman numeral tuples list
    dig_to_roman = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),
                    (90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),
                    (4,"IV"),(1,"I")]
    #list that will hold roman letters as they're added
    roman_digits = []

    for value, symbol in dig_to_roman:
        #break the loop if we have already found the highest integer
        if num == 0:
            break
        count, num = divmod(num,value)
        #append the right number of symbols to roman_digits
        roman_digits.append(symbol*count)
    #once loop is broken join the roman numerals into one string and return it
    return "".join(roman_digits)
intToRoman(25)
intToRoman(3888)

#Length of the last word in a sentence
def lengthOfLastWord(s):
    #split the incoming sentence into a list of words
    sentence = s.split()
    #return the length of the last word by popping it off and using len()
    return len(sentence.pop())
lengthOfLastWord("Hello World")
