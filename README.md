# Wiki Revision history scrap

Wiki Revision history scrap using Beautiful soup and pandas libraries and exporting it to a csv file.

This code can be used to crawl wikipedia revisions history data. 
I needed "Date" "Time" "user" "minor edits or not" "# of bytes changed" for a project. 

For example in the link below: 
https://en.wikipedia.org/w/index.php?title=United_States&offset=20030729010851%7C1215590&limit=500&action=history 


We can see the revisions:

![](img/webscrapB.PNG)


Using the code, I have extracted the following:

![](img/webScrapA.PNG)

I needed my data in reversed order. So I used reversed function in my loop. You can modify it according to your needs.
