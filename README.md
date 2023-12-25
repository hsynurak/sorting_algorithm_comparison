# sorting_algorithm_comparison

We have defined the random library to obtain random numbers, the time library to calculate sorting times, and the matplotlib.pyplot library to visualize the data on graphs.

Functions named "insertion_sort" and "merge_sort" contain sorting algorithms.

The lists "arr_merge_time" and "arr_insert_time" will store the processing times obtained in the ongoing sections.

In the for loop, we specify the number of elements one by one between 1 and 1000.

The code line `arr = random.sample(range(1, 1001), i)` uses the `sample()` function from the random library. We specified the range of random numbers to be taken as the first parameter of the sample() function, and then, with the value of i from the for loop containing this code line, we determined how many elements would be taken.

The code lines `start = time.time()` and `end = time.time()` record the start and end times according to the current time using the time() function from the time library.

The lines `merge_time = round(end - start, 6)` and `insert_time = round(end - start, 6)` calculate the processing times by taking the difference between the start and end times for merge and insert sort operations, respectively. We used the round() function to limit the number of decimal places for readability.

The lines `arr_merge_time.append(merge_time)` and `arr_insert_time.append(insert_time)` place the obtained processing times into the empty lists we created earlier.

The lines “plt.plot(range(1, 1001, 1), arr_insert_time, label='Insertion Sort', color='red')” and “plt.plot(range(1, 1001, 1), arr_merge_time, label='Merge Sort', color='blue')” reflect the values of the two operations one by one on the graph. The first variable represents the x-axis, indicating the number of elements in the array being processed. The second variable represents the y-axis, indicating the processing time. The third variable customizes the colors of the reflected data on the graph.

The lines “plt.xlabel('Array Size')” and “plt.ylabel('Time (seconds)')” are used to provide titles indicating what the data on the x and y axes represent.

The line “plt.title('Merge Sort(blue) vs Insertion Sort(red)')” is used to add a general title to the graph.

The line `plt.show()` is the command to run the graph.



The point marking code is used to visually highlight the intersection point where the execution times of insertion sort and merge sort are approximately equal. he enumerate function is used to iterate over the pairs of elements from arr_insert_time and arr_merge_time along with their indices (idx). The intersection index is stored in the variable intersection_index. 
![Uploading image.png…]()
