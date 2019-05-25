## Data vs information ##
**Data** is the set of record, which haven't been process, in this stage, you cannot discover in those choas record.
<br>**Infromation** is the processed Data, which can be discover something, and learn something from that.

## Data Type ##
**Primitive Data Type:** just basic data type, such as integer, float or bool.
**<br>Structured Data Type/Virtual Data Type:** Which is higher dimension than the upper one, includes string, array, pointer, list, and file 
**<br>Abstract Data Type(ADT):** You can call it's a set of previous record, example for that are Stack(FILO structure), and Queue(FIFO structure), also we have Arraylist in Java(Both Stack and Queue combination)

## Type of Data structure ##
**Array:** `a=[1,2,3,4,5,6,7,8,9,10]`
**<br> Two-dimension Array:** `ar=[i][j]/ar=[[1,2,3],[4,5,6],[7,8,9]] -> ar=[0][1]=2`
**<br> Three-dimension Array:** `arr[i][j][k]/arr=[[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16]]] -> arr[0][0][2]=3`

**<br>Linked List:**

<img src="Linked_list_sample.jpeg" alt="drawing" width="400" height="200"/>


**<br>Stack:<br>**
**FILO Structure<br>**
**Function:** create, push, pop, isEmpty, full<br>
**Create:** Create a empty Stack, return a Stack object<br>
**Push:** store the data on top of the stack, return null<br>
**Pop:** Remove the data on top, return the first Data<br>
**isEmpty:** Check the stack empty or not, return boolean<br>
**Full:** Check the stack full or not, return boolean<br><br>
<img src="stack.png" alt="drawing" width="300" height="200"/>

**<br>Queue:<br>**
**FIFO Structure<br>**
**Function:** create, add, delete, front, empty<br>
**Create:** Create a queue Stack, return a queue object<br>
**Add:** Store the data on tail of the queue, return null<br>
**Delete:** Remove the data on front of the queue, return null<br>
**front:** Obtain the data on front of the queue, return the first record of the Queue<br>
**Empty:** Check the queue empty or not, return boolean<br><br>
<img src="Queue.png" alt="drawing" width="300" height="200"/>

**<br>Tree Structure(BST):<br>**
<img src="binary_tree.jpg" alt="drawing" width="400" height="200"/>

**Hash table:<br>**
Using for store the file signature, or define as a content list
**<br>Function:**
**<br>Bucket:** Using for store the data record, one bucket will store a lot of slot
**<br>Slot:** The address in the bucket
**<br>Collision:** The output of the hash same as other existing hash, which could becomea huge problem.
<img src="hash_table.png" alt="drawing" width="400" height="250"/>
                                                                                                                                                         