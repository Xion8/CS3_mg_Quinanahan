### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section:          9-Magnesium    	Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name:  12 / Quinanahan 	Date:  August 26, 2026**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

Implementation 2 is the faster algorithm when the list has number which are very large because, it starts from the middle of the list and checks if the value is more or less than the middle value, unlike implementation 1 which uses a for loop, where it takes the first number and individually checks all the numbers, making it slower than implementation 2 when it comes to large lists.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list?~~ | ~~How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list?~~ |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

At first glance implementation is easier to understand as it uses very simple code, where it uses a for loop to check each variable one by one.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process?~~ | ~~How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process?~~ |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

Implementation 1 would be much easier to update because it uses simple and few lines of code like for loops, and it also is less likely to have errors. Unlike Implementation2 which has a much more complex code making it easier to have errors in creating and adding new lines of code.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating?~~ | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

Implementation 1 would be easier to test with different inputs as it benefits in searching through smaller lists, where it checks through each variable. But the downside to this would be that it takes a long time to check through long lists where Implementation 2 is actually better, as it can efficiently go through longer lists and has fewer conditions to check.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ | Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?

The algorithm should check for empty lists, check and verify if the data types are valid, and check for other index errors, to make sure that the algorithm will be able to end and complete the program.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search?~~ | ~~Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search?~~ |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

I would choose implementation 2 as it is more efficient when it comes to larger numbers, and organized lists, while implementation 1 is better when it comes to unsorted lists, and smaller lists.