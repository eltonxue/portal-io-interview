# portal-io-interview

Task 3:

For my choice of data structure, I decided to utilized a 2D list and Unix timestamps to display scheduling data with the first index representing the title given for the event, the second index representing the start time in Unix timestamps, and the third index representing the end time in Unix timestamps. The reason why I decided to use Unix timestamps was because it simplifies the whole process of finding conflicts by eliminating conversion calculations needed to compare start and end times.

For my algorithm, I sorted the given data structure based on the start times of each event and looped through the sorted list using indexes. After that, I compared the current end time with the previous end time and reassign it if it is larger. The reason why I do this is because I have to take into consideration the larger end time to find conflicts. Lastly, I compared the current start time with the end time, adding the the events that have the start time lower than the end time. I also used a set for its ability to not contain any duplicates.

The algorithm I used is is O(N Log N) because I used the basic sorting function. Initially, I thought of using two for loops, which would work. However, the complexity class would be less efficient at O(N^2). To test my answer, I calculated conflicting interval test cases and all the conflicts for my specific events. However, this algorithm should work for others.
