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

# Add two numbers that are stored 2 linked lists in reverse order
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1,l2):
    dummyHead = ListNode(0)
    curr = dummyHead
    carry = 0 #variable for when the sum of 2 digits exceeds 10
    #loop that will continue while there are still digits in either of the two
    #lists or the carry is not 0
    while l1!=None or l2!=None or carry!=0:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        columnSum = l1Val+l2Val+carry
        carry = columnSum/10 #if below 10 it will be 0
        newNode = ListNode(columnSum%10)
        curr.next = newNode
        curr = newNode
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummyHead.next
l1 = ListNode(0)
l2 = ListNode(0)
addTwoNumbers(l1,l2)

# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in
# left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
def plusOne(digits):
    for i in range(len(digits)):
        idx = len(digits)-1-i
        #set all digits that are equal to 9 to 0
        if digits[idx]==9:
            digits[idx] = 0
        #the right most digit that isn't a 9
        else:
            digits[idx]+=1
            return digits
    # we get here if all digits are 9
    return [1]+digits
plusOne([9,9,9])
plusOne([5,4,3,9,9])

# Given two binary strings a and b, return their sum as a binary string.
def addBinary(a,b):
    n = max(len(a),len(b))
    a,b = a.zfill(n), b.zfill(n)

    carry = 0 #this variable will decide what is appended to the answer
    answer = []
    for i in range(n-1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1
        if carry%2 == 1:
            answer.append('1')
        else:
            answer.append('0')
        carry //= 2
    if carry == 1:
        answer.append('1')
    #answer needs to be reversed because everything was added to the end of the
    #array when the addition is done from right to left
    answer.reverse()

    return ''.join(answer)
addBinary('0111','1110')
