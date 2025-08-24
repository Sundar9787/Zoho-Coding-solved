'''Write a program to find out and display prime numbers from the given list of integers. The program will accept input in two lines.
First-line contains a number indicating the total number of integers in the list and the second line contains integers separated by spaces.'''
no_elements = int(input('No of elements: '))
arr= list(map(int, input('Enter elements: ').split()))
result=[]
def solution(arr):
    for num in arr:
        count = 0
        for i in range(1,num+1):
            if num%i==0:
                count = count + 1 
        if count <= 2:
            result.append(num)
            
            
    return result
        
print(solution(arr))
