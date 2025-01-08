______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Legend to Organizational Formatting of Document:

A.	The section breaks / isolation bars ______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________ 

purely denotes a section break entirely from one complete section to another unrelated to it before or after. Isolates given collected information by groups almost like page breaks or horizontal lines.
These service no function but are to visually help me structure and organize this into easier to manage information all in one document.

B.	Anything wrapped in angle brackets <> denotes as that sections header to identify what content is within that section. 

C. Anything wrapped in regular brackets [] denotes sub-headings. Think of <> as H1 and [] as H2. Or <> as H2 and [] as H3. Hierarchial headings.


______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<Instructions to simplify completing tasks and course project easier, simpler and more quickly>

It's broken into 2 parts, a planning task (Task 1) and an implementation step (Task 2).

I used pycharm community edition to write my program for Task 2 and I would recommend it. This task is where I think I could have saved some time. I tried a couple ways of setting things up before ultimately getting everything working only to find the implementation guide that explained it all exactly as I had eventually done it.

I definitely recommend looking over the implementation guides, also found in the supplemental resources page, and follow along with one of them. I used a nearest neighbor algorithm so rather than restating the implementation guide I'll just point out a few things I did differently.

The following steps refer to steps in the nearest neighbor implementation guide.

In step A, rather than creating CSV files, I manually imported the data from the package info and distance table provided. I'm sure it's not difficult to make the CSV files and there are videos on how to do that. I just opted to copy and paste the data into my project as I am extremely lazy and the csv files are not a requirement. I put the package data into package objects which were later imported into my hash table.

For step B again rather than use CSV files to populate the 2D list I just copied and pasted data from the excel form.

On step C I opted to load the trucks manually as there is no requirement to make an algorithm to load the trucks (however I'm sure it makes your program look more impressive). I created 3 lists of package id's and used that as an input to load the trucks and was able to make sure all requirements/special instructions were met.

D is your actual delivery algorithm. My algorithm ended up matching the implementation guide very closely. Just going to the closest address and removing the package(s) that need to go there while also updating truck mileage and package status.

For E I used a simple, while input is not 'exit', loop with an if, elif... for each of the options which are given to the user as an initial prompt when running.

There is a linkedin learning course that is about 5 hours, however python is pretty user friendly in my opinion. I was able to get away with just the knowledge I learned in DS and Algorithms I along with some googling of python syntax.

The screenshots for task 2 are mostly self explanatory. I did mine in the windows command prompt but I'm sure in pycharm would be fine too.

To find other algorithms you could have used just look up possible solutions to the traveling salesmen problem as that is the problem this project covers.

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<Also a second set of Instructions to simplify completing tasks and course project easier, simpler and more quickly>

suggested thinking of this project from an object-oriented Java point of view. That's when it really clicked.

When I was looking at the projects on GitHub, none of them were using object classes. They were using arrays and hash maps for every little thing, when instead, these things could be attributes of a class object. My project consists of 261 lines of code when you account for the blank lines between methods and the comments, and there are plenty of comments. 261 lines of code is less than half of the lines of code of the projects I saw online. 261 lines of code does not include the CSV files.

Here's what you do if you want to tackle this project with an object-oriented mindset.

Take the excel data files and strip them of all the words/characters that are not specific data points. Then convert the files into CSV.

Create a Truck python file

Create a Truck class and define the attributes. Unlike Java you don't need setters and getters

There will be a def init and a def str to define the class

Create a Package python file

Like the truck class, define the package object with def init and a def str

In the Package object class I created a method to determine the package status of: at hub, en route, delivered - 7 lines of code

Create a "create hash map" Python file

You can find examples of this in the book, in the code repository, and all over the internet

I copied the hash insert function from the code repository. In my code I made this comment to cite: # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py - 10 lines of code, not including blank lines and comments

Create a Main Python file

Most of the code is in the main file; my main file is 175 lines of code (including comments and blank lines)

This file is hard to explain without showing you my code -> GitHub Link, https://github.com/FallicoFunctions/Python-Mail-Delivery-Service-Algorithm_WGU-C950

You will need methods to open/read the CSV files - 3 lines of code for each method

Instantiate a hash map for package objects - 1 line of code

You will need a method to load the package attributes from the CSV files; I found this method in the code repository file W-3_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy_Dijkstra.py on line 98 - about 18 lines of code including blank lines and comments in the method

Create a method to find the distance between two addresses. This method will read the Distances CSV file. It will take in an x-value and a y-value. It will use that to find a number by row and column in the CSV file - 6 lines of code including a blank line in the method

Create a method to extract an address from the Address CSV file. Uses a for-loop and an if-statement in that loop - 4 lines of code

Instantiate 3 truck objects - 1 line of code each

Manually load the trucks within the truck instantiation. One of the attributes for the truck class is an array of packages. When you instantiate the truck you can place the object IDs into each truck. EX: mail_truck_1 = Truck.Truck(int speed, int mileage, str current address, packages [1, 3, 6, 48], etc)

Create a method for the nearest neighbor algorithm. It is a lot simpler than you think. Meet with your instructor if you need help on this. With using Truck objects, this algorithm method will place the packages in order, record how many miles the route is, and determine the time each package is delivered. This method will passthrough one truck object. After the method is written call it three times, once for each truck object - 20 lines, not including comments and blank spaces.

*Create the command line interface. This is where the Class Main will be defined. The user interface is one big if-statement with a nested if/elif-statement. The program first asks for a time, then it asks if you want to lookup a single package tracking info or all packages at once. Then the data is displayed and the program quits itself - 38 lines not including comments

Comment questions from others:

I am working on this course right now. Everything is being defined in classes except the code in main.py; it makes keeping track of things so much easier!. I don't know how the hell I programmed anything useful before I learned object-oriented programming. 

How did you handle the special notes for the packages? I don't seem to see it in the Package class. To me this seems like the hardest part - making sure that the right packages are delivered together, making sure they are picked up after 10:30, etc.

It's been a while since I've thought about this. I manually loaded the trucks so I could put certain packages together based on the requirements. For example, I think I put all the late packages on truck 3.


His GitHub Repo Page for his C950 Project: https://github.com/FallicoFunctions/Python-Mail-Delivery-Service-Algorithm_WGU-C950/tree/master


______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


<Non-specific, unsorted, unordered comments and notes I thought were relevant enough to stick in here to be included and made aware of too>

The old version of the course had a rubric walkthrough - in it the instructor says you don't need to worry about accounting for collisions in your hash table.
It isn't mentioned on the current rubric but they DO want you to address this.

Note that it is no longer true that K2 can include modifications to the hash table.
You must discuss 2 different data structures that are independent of your hash table solution.

While not required by the task, it is highly recommended that you state in your task 2 documentation which version of Python you used. 
We've had some issues with evaluators not having a new enough version and therefore getting errors when trying to run student code.


<Python version is 3.13.1 and IDE is Pycharm Professional 2024.3.1.1>
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<C950 WGUPS Project Implementation Steps - Example - Nearest Neighbor>

'''

C950 WGUPS Project - Implementation Steps - Start

Please note; this is an example of implementation utilizing Nearest Neighbor Greedy Algorithm.

Feel free to use it by citing this document, however it is highly recommended that you come up with your own approach

---------------------------------------------------------------------------------------------

A) Package data steps:

1-Create HashTable data structure (See C950 - Webinar-1 - Let’s Go Hashing webinar)

2-Create Package and Truck objects and have packageCSV and distanceCSV and addressCSV files ready

3-Create loadPackageData(HashTable) to 

- read packages from packageCSV file (see C950 - Webinar-2 - Getting Greedy, who moved my data  webinar) 

- update Package object

- insert Package object into HashTable with the key=PackageID and Item=Package

 

B) Distance data steps:

B.1) Upload Distances:

4-Create distanceData List

5-Define loadDistanceData(distanceData) to read distanceCSV file 

- read distances from distanceCSV file; row by row

- append row to distanceData (two-dimensional list. See C950 WGUPS Distance Table Matrix)

B.2) Upload Addresses:

6-Create addressData List 

7-Define loadAddressData(addressData) to read addressCSV file

- read only addresses from addressCSV file

- append address to addressData. 

 

C) Algorithm to Load Packages:

C.1) Function to return the distance between two addresses:

8-Define distanceBetween(address1, address2)

9-Return distanceData[addressData.index(address1)][addressData.index(address2)]

   i.e. distances between addresses can be accessed via distanceData[i][j]; 

C.2) Function to find min distance/address:

10-Define minDistanceFrom(fromAddress, truckPackages)

11-Return min distance address to fromAddress 

   i.e. call distanceBetween(address1, address2) in a loop for all the addresses in the Truck

C.3) Function to load packages into Trucks:

12-Define truckLoadPackages()

13-Load Trucks based on assumptions provided (ex. Truck-2 must have some packages, some packages go together, some packages are delayed, ...)

14-And closest addresses/packages until there is 16 packages in a Truck

  i.e. Load manually/heuristically or Loop package addresses and call minDistanceFrom(fromAddress, truckPackages) for all the addresses in the Truck not visited yet

 

D) Algorithm to Deliver Packages:

D.1) Function to deliver packages in a Truck:

15-Define truckDeliverPackages(truck)

16-Loop truck package addresses and call minDistanceFrom(fromAddress, truckPackages) for all the addresses not visited yet

D.2) Keep track of miles and time delivered:

17-Update delivery status and time delivered in Hash Table for the package delivered and keep up with total mileage and delivery times. 

    i.e. How to keep track of the time?:

    timeToDeliver(h) = distance(miles)/18(mph) where 18 mph average Truck speed. 

    time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)). time_obj could be cumulated to keep track of time.

 

E) UI to Interact with the Users:

18-Create an UI to interact and report the results based on the requirements. 

 

Possible Menu Options:

***************************************

1. Print All Package Status and Total Mileage       

2. Get a Single Package Status with a Time

3. Get All Package Status with a Time 

4. Exit the Program               

***************************************

 

Possible output example:

PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime

1, 195 W Oakland Ave, Salt Lake City, UT, 84115, 10:30 AM, 21, , ... Delivered by Truck-2, 08:46:20

2, 2530 S 500 E, Salt Lake City, UT, 84106, EOD, 44, , ... AtHub

3, 233 Canyon Rd, Salt Lake City, UT, 84103, EOD, 2, Can only be on truck 2, ... InRoute by Truck-2

...

...

...

 

C950 WGUPS Project - Implementation Steps - End

---------------------------------------------------------------------------------------------

'''

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<Aside from official rubric documents which are the only true source of official requiremenst and are what evaluators literally use as a checkoff list,
The following is a comprehensive collection of main instructions, information, and suggestions overall laid out more plainly by the course instructors first as an outline/template only, then as a fully commented on instructional template with detailed directions>
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<Task 2 Template>

[SCENARIO]

The Western Governors University Parcel Service (WGUPS) needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

Your task is to determine an algorithm, write code, and present a solution where all 40 packages (listed in the attached “WGUPS Package File”) will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for both trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map,” and distances to each location are given in the attached “WGUPS Distance Table.” The intent is to use the program for this specific location and also for many other cities in each state where WGU has a presence. As such, you will need to include detailed comments to make your code easy to follow and to justify the decisions you made while writing your scripts.

Keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and at what time the delivery occurred.

[ASSUMPTIONS]

•   Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
•   The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
•   There are no collisions.
•   Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that truck is in service.
•   Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. 
•   The delivery and loading times are instantaneous, i.e., no time passes while at a delivery or when moving packages to a truck at the hub (that time is factored into the calculation of the average speed of the trucks).
•   There is up to one special note associated with a package.
•   The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S State St., Salt Lake City, UT 84111) until 10:20 a.m.
•   The distances provided in the WGUPS Distance Table are equal regardless of the direction traveled.
•   The day ends when all 40 packages have been delivered.

[REQUIREMENTS]

A.  Identify a named self-adjusting algorithm (e.g., “Nearest Neighbor algorithm,” “Greedy algorithm”) that you used to create your program to deliver the packages.

B.  Write an overview of your program, in which you do the following:
1.  Explain the algorithm’s logic using pseudocode.

2.  Describe the programming environment you used to create the Python application.
3.  Evaluate the space-time complexity of each major segment of the program, and the entire program, using big-O notation.
4.  Explain the capability of your solution to scale and adapt to a growing number of packages.
5.  Discuss why the software is efficient and easy to maintain.
6.  Discuss the strengths and weaknesses of the self-adjusting data structures (e.g., the hash table).

C.  Write an original program to deliver all the packages, meeting all requirements, using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and the “WGUPS Package File.”
1.  Create an identifying comment within the first line of a file named “main.py” that includes your first name, last name, and student ID.
2.  Include comments in your code to explain the process and the flow of the program.

D.  Identify a self-adjusting data structure, such as a hash table, that can be used with the algorithm identified in part A to store the package data.
1.  Explain how your data structure accounts for the relationship between the data points you are storing.

Note: Use only appropriate built-in data structures, except dictionaries. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the Internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.

E.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the following components as input and inserts the components into the hash table:
•   package ID number
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   delivery status (e.g., delivered, en route)

F.  Develop a look-up function that takes the following components as input and returns the corresponding data elements:
•   package ID number
•   delivery address
•   delivery deadline
•   delivery city
•   delivery zip code
•   package weight
•   delivery status (i.e., “at the hub,” “en route,” or “delivered”), including the delivery time

G.  Provide an interface for the user to view the status and info (as listed in part F) of any package at any time, and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)
1.  Provide screenshots to show the status of all packages at a time between 8:35 a.m. and 9:25 a.m.
2.  Provide screenshots to show the status of all packages at a time between 9:35 a.m. and 10:25 a.m.
3.  Provide screenshots to show the status of all packages at a time between 12:03 p.m. and 1:12 p.m.

H.  Provide a screenshot or screenshots showing successful completion of the code, free from runtime errors or warnings, that includes the total mileage traveled by all trucks.

I.  Justify the core algorithm you identified in part A and used in the solution by doing the following:
1.  Describe at least two strengths of the algorithm used in the solution.
2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
3.  Identify two other named algorithms, different from the algorithm implemented in the solution, that would meet the requirements in the scenario.
a.  Describe how each algorithm identified in part I3 is different from the algorithm used in the solution.

J.  Describe what you would do differently, other than the two algorithms identified in I3, if you did this project again.

K.  Justify the data structure you identified in part D by doing the following:
1.  Verify that the data structure used in the solution meets all requirements in the scenario.
a.  Explain how the time needed to complete the look-up function is affected by changes in the number of packages to be delivered.
b.  Explain how the data structure space usage is affected by changes in the number of packages to be delivered.
c.  Describe how changes to the number of trucks or the number of cities would affect the look-up time and the space usage of the data structure.
2.  Identify two other data structures that could meet the same requirements in the scenario.
a.  Describe how each data structure identified in part K2 is different from the data structure used in the solution.

L.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

M.  Demonstrate professional communication in the content and presentation of your submission.

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


<Same Task 2 Template But The Instructional Information Has Been Replaced With Comments, FAQ and Additional Info>

[Scenario]

The Western Governors University Parcel Service (WGUPS) needs to 
determine the best route and delivery distribution for their Daily Local 
Deliveries. The Salt Lake City DLD route has three trucks, two drivers, and 
an average of 40 packages to deliver each day; each package has specific 
criteria and delivery requirements. 
 
Your task is to write code that determines and presents a solution delivering 
all 40 packages, listed in the attached “WGUPS 
Package File,” on time, according to their criteria while reducing the total 
number of miles traveled by the trucks. The “Salt Lake 
City Downtown Map” provides each address’s location, and the “WGUPS 
Distance Table” provides the distance between each address (note: mileage 
on the distance files may not match distances on the map). 
The supervisor (user) needs the means to check the status of any given 
package at any given time using package IDs. The report should also include 
the delivery times, which packages are at the hub, and en route. The intent 
is to use this program for this specific location and use the same program in 
different cities as WGUPS expands its business. As such, you will need to 
include detailed comments following the industry-standards to make your
code easy to read and justifying the decisions you made while writing your program.

[Project Summary]

You will write a program in Python, which does the following: 
- Can store the package information into a hash table. 
- Uses a self-adjusting heuristic algorithm to find a solution that delivers 
all packages using under 140 miles and according to the provided 
requirements (e.g., delivery deadlines, addresses, number of trucks, 
special notes, etc.). 
Note: Non-self-adjusting methods are also allowed, but there 
must be at least one part that uses a self-adjusting algorithm 
(identified in Part A) with one scalable element (discussed in Part 
B4). 
- Allows the ‘user’ to check the status (at the hub, en route, or delivery 
time) of any package at any given time. 
Using code comments and a separate document, complete the following: 
- Provide code comments for every significant portion of code that 
explains the logic and timecomplexity. 
- Provide documentation on algorithms used, alternative methods to, 
efficiency, and scalability of the methods used to find a solution. 
- Provide documentation on the data structure(s) describing their use, 
alternative methods, efficiency, and scalability of data processes.

[Technical Requirements and Resources]

Evaluators need to successfully run your code using only submitted 
files and the most recent version of Python. Submitted code may use 
anything from Python’s standard library, including the built-in data 
structures (e.g., lists, tuples, sets, and dictionaries), except for the hash 
table where only the use of dictionaries is prohibited. 
- The project must use the package, and distance data provided in files 
WGUPS Distance Table.xlsx and WGUPS Package Table.xlsx found in 
‘View Task>Task Overview>Supporting Documents’ on the C950 COS 
page. You may make minor changes (such as removing headers) and 
convert these documents into ‘.csv.’ files.
Note: there is one minor differences between the addresses in the package and distance files:
Distance file: 
5383 S 900 East 
#104 (84117) 
Package file: 
5383 South 900 
East #104
- Submitted code may use anything from Python’s standard library,
including the built-in data structures (e.g., lists, tuples, sets, and 
dictionaries). The only exception is the hash-table, where the use of 
dictionaries is prohibited (a dictionary is a hash-table).

[Recommendations]

- We recommend using the PyCharm IDE. You can simply zip and 
upload your project folder when you submit your project. 
- Organize your document so that it specifically addresses the rubric 
requirements. For example: 
Typically 2-3 sentences suffice per section. This way makes it easier 
to write, grade, and fix if necessary. Mention everything in the rubric 
requirements, even if it’s redundant or superfluous. 
The coding/annotations sections of the directions are only suggestions.

[Assumptions]

- Two drivers and three trucks are available. So no more than two trucks 
can be away from the hub at the same time. 
- The trucks move at a constant speed of 18 miles per hour. 
- Trucks can carry a maximum of 16 packages. 
- Trucks can leave the hub no sooner than 8:00 a.m. 
- Trucks can be loaded only at the hub. 
- You only need to account for the time spent driving. You can ignore the 
time spent on all other activities, such as loading trucks and dropping 
off packages. 
- The wrong delivery address for package #9, Third District Juvenile 
Court, will be corrected at 10:20 a.m. The correct address is “410 S 
State St., Salt Lake City, UT 84111”. You may assume that WGUPS 
knows the address is correct and when the correction will be available.
- Packages #13, #14, #15. #16, #19, and #20 must go out for delivery 
on the same truck. 
- Packages #3, #18, #36, and #38 may only be delivered by truck 2. 
- #6, #25, #28, #32 cannot leave the hub before 9:05 a.m.

[Comments on evaluations]

- Evaluators grade, using the rubric as a checklist. Submissions 
minimally meeting specific requirements of the rubric typically pass. 
- Evaluators are required to respond using the following format: 
- Acknowledge anything written attempting to address the rubric 
section (even if incorrect or irrelevant). 
- State what is missing or incorrect addressing the rubric section. 
- Automatically mark sections as “Not Evident,” i.e., red, if a 
dependent section does not pass. For example, if Part A is 
missing, Parts I1-I3A may be marked “red” automatically. 
- If an evaluator writes “insufficient details…” (or something similar), the 
entry is typically close to being accepted -they just need more. 

[Rubric Requirements Summary]

Note: The official rubric is the final say on what is required to pass; evaluators 
use it as a checklist. The sections below paraphrase or restate the official 
rubric for better readability and alignment with general evaluation practices. 
Submissions minimally meeting specific requirements of the rubric typically 
pass. You can find the official rubric on your C950 COS page. 
A: ALGORITHM SELECTION 
Identify by name the self-adjusting algorithm used to create a program to 
deliver the packages and meet all requirements specified in the scenario. 
You must identify the self-adjusting part(s) of your algorithm by name. 
Though you may have written your algorithm using a variety of approaches, 
you should be able to connect or generalize part of your algorithm to a 
commonly recognizable method, e.g., a greedy algorithm, farthest neighbor 
algorithm, etc. 
What is self-adjusting? Any code which adjusts dynamically according to 
input, i.e., you give the code package info, and the code makes decisions. 
For example, if you manually choose ten packages and then your code 
decides how to deliver those packages, 
- The code choosing the packages is not self-adjusting. 
- The code deciding how to deliver the packages is adjusting. 
The identified (also called “chosen” in Part I1 of the rubric and “core” in Part 
I of the directions) algorithm must be self-adjusting. Using non-self-adjusting 
methods is acceptable, but at least one part must use a self-adjusting 
algorithm. 
B1: LOGIC COMMENTS 
The submission accurately explains the algorithm’s logic using pseudocode. 
Provide an outline of how your code finds a solution. You can do this in your 
document or code comments, though we recommend the former. 
There is no formal way to write pseudocode (or it would not be pseudocode). 
Following the example found in the sample algorithm document is one way 
to fulfill this requirement. Still, you certainly need a step-bystep explanation 
(via pseudocode or bullet points) outlining how your code finds a solution. 
B2: DEVELOPMENT ENVIRONMENT 
The submission accurately describes the software and hardware used to 
create the Python application. 
You should include brief descriptions of the programming language, IDE, 
operating systems, hardware, etc., used to write and run your application. 
B3: SPACE-TIME AND BIG-O 
The (code) submission accurately describes the space-time complexity for 
each major block of code and the entire program using Big-O notation. 
Include this in code comments. “Major block” of codes and “accuracy” is not 
defined. Ask yourself, “if I was looking at this code for the first time, what 
would I want to be described? How much detail would I need?” 
How accurately does the time complexity description need to be? Big-O 
classifications are sets of functions defined by an upper bound. e.g., a 
function that is in O(1) is also in O(n). However, it is reasonable for 
evaluators to expect better accuracy in obvious cases, e.g., if it’s constant -
write O(1). For more complicated situations, less accuracy should be 
acceptable. 
If you are uncertain about whether comments or accuracy is sufficient -
submit it. At worst, the evaluator will ask for more. 
B4: ADAPTABILITY 
The submission application accurately explains the application’s capability to 
scale and adapt to an increasing number of packages. 
The application will have at least two scalable elements, the self-adjusting 
algorithm from Part A and the self-adjusting data structure (hash-table) from 
Part D. The discussion can also include shortcomings, e.g., 
“X will not scale well because…” 
B5: SOFTWARE EFFICIENCY AND MAINTAINABILITY 
The discussion addresses how the software is efficient and easy to maintain. 
By “efficiency,” they mean the Big-O time complexity of your entire program. 
Your program must run in polynomial time or better to be efficient. 
For “maintainability,” describe how future developers can easily understand, 
repair, and enhance your code, i.e., -software maintainability—for example, 
code structure, comments, compartmentalization, etc. 
B6: SELF-ADJUSTING DATA STRUCTURES 
The discussion addresses the strengths and weaknesses of the selfadjusting data structures (including the hash-table). 
Include all self-adjusting (non-builtin) data structures in the discussion. 
However, you are only required to have one such data structure -the hashtable from Part D. The rubric specifies “strength-s” and “weaknesses.” So 
include at least two for each. 
C: ORIGINAL CODE 
The code is original and runs without errors or warnings. 
The code should run using a standard installation of the latest version of 
Python 3. The evaluators should not need to download any libraries, e.g., 
pandas. Most submissions run through an IDE; evaluators will use PyCharm. 
So if you do something different, say running it through the console, consider 
including special instructions. 
C1: IDENTIFICATION INFORMATION 
The initial comment within a file named “main.py” includes your first name, 
last name, and student ID. 
Include these comments in a “main” file. Easy to satisfy, but easy to forget! 
Also, as this section requires a “main.py” file, it makes sense to have this file 
be your application’s entry point. Though it is not required, if you do 
something different, provide specific instructions on how to run your 
application. 
C2: PROCESS AND FLOW COMMENTS 
Include comments within the code adequately explaining the process and 
flow of the program. 
Explain the intent and decisions of each “major” block of code, i.e., the 
“why, what, and how.” The comments should improve readability. Provide a 
little more detail for any process that is unusual or complicated. 
This can be done alongside comments satisfying Part B3. Similarly, which 
parts require explanation and what qualifies as “adequately” is highly 
subjective. Ask yourself, “if I was looking at this code for the first time, what 
would I want to be described? How much detail would I need?” 
D: DATA STRUCTURE 
The submission identifies a self-adjusting data structure that can store the 
package information and perform well with Part A’s algorithm. 
As with Part A, self-adjusting means any code which adjusts dynamically 
according to input. This can include adjusting to size (lists are mutable in 
Python) or searches. For example, a hash table that can adapt to more 
packages without rewriting the code would be self-adjusting. This data 
structure must be the same hash-table in Part E and Part F. Nothing else 
regarding the complexity of your hash table is required, e.g., it can be a 1-1 
mapping, does not have to handle collisions, have chaining, etc. 
The official task directions include a note: 
“Note: Use only appropriate built-in data structures, except 
dictionaries.”
Submitted code may use anything from Python’s standard library, including 
the built-in data structures (e.g., lists, tuples, sets, and dictionaries). The only 
exception is the hash-table, where the use of dictionaries is prohibited (a 
dictionary is a hash-table). 
Per parts E and F, the hash table must have the following: 
- E: an insertion function that includes as input all a package’s info (see 
below). 
- F: a look-up function that uses the package’s ID as input and returns 
the corresponding package’s information (see below). 
The ability to store and retrieve package info (via the package’s ID) is the 
only requirement. The information can be stored in an object and include 
additional parameters, e.g., special notes, time the package left the hub, etc. 
The insert function (Part E) and look-up function (Part F) must respectively 
store and retrieve the following information: 
- package ID number 
- delivery address 
- delivery deadline 
- delivery city 
- delivery zip code 
- package weight 
- delivery status (at the hub, en route, or delivery time) 
D1: EXPLANATION OF DATA STRUCTURE 
The submission accurately explains how the data structure (hash-table) uses 
package IDs to store and retrieve package information. 
Provide an explanation that describes the hash table’s logic, i.e., how it 
stores and retrieves package information. You should include a description 
of why your hash-table retrieves information accurately and more efficiently 
than a simple linear search. 
E: HASH TABLE 
The hash table has an insertion function that stores all of the given 
components (listed in Part D) using the package ID as the key.
F: LOOK-UP FUNCTION 
The provided hash table should include a look-up function that can use a 
package's ID to retrieve all of the same package’s components from the hash 
table (listed in Part D). 
The package ID must be the key, and the components from Part D must be 
the values. There are no other specifications, and you can choose how the 
values within the hash-table are stored. For example, the components could 
be in an object or a different data structure of your choosing. 
G: INTERFACE 
Provide an intuitive interface for the user to view the status and information 
(as listed in Part D) of any package at any time and the total mileage traveled 
by all trucks. The delivery status should report the package as “at the hub,” 
“en route,” or “delivered at ____.” Delivery status must include the time. 
This can be done through a simple console interface (it might be preferable). 
The evaluators need an easy way to check that all packages were delivered 
according to their constraints using under 140 miles. 
“Intuitive” means that evaluators can do this through the interface without 
reading your code. 
To check package statuses, you should be able to enter a time and check 
all packages’ statuses (delivered at X, at the hub, or en route). 
Possible Menu Options: 
*************************************** 
1. Print All Package Status and Total Mileage 
2. Get a Single Package Status with a Time 
3. Get All Package Status with a Time 
4. Exit the Program 
*************************************** 
Possible output example: 
PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, 
PageSpecial Notes, Status, DeliveryTime 
1, 195 W Oakland Ave, Salt Lake City, UT, 84115, 10:30 AM, 21, , ... 
Delivered by Truck-2, 08:46:20
2, 2530 S 500 E, Salt Lake City, UT, 84106, EOD, 44, , ... AtHub
3, 233 Canyon Rd, Salt Lake City, UT, 84103, EOD, 2, Can only be on truck 
2, ... InRoute by Truck-2
... ...
G1-G3: 1st, 2nd, and 3rd status checks. 
Provide screenshots showing the information (as listed in Part D) and 
statuses (see Part G) at a time between: 
- 8:35 a.m. and 9:25 a.m. 
- 9:35 a.m. and 10:25 a.m. 
- 12:03 p.m. and 1:12 p.m. 
Provide one screenshot within each of the time intervals above. If everything 
does not fit on a single screenshot, you can use multiple images; label them, 
so it’s clear which time interval they cover, e.g., “G1-
a.jpg, G1-b.jpg,...” The screenshots can be included anywhere in your 
submission, e.g., the document, separately, in the project folder -but make 
them easy to find. 
H: SCREENSHOTS OF CODE EXECUTION 
Provide a screenshot or screenshots showing the total delivery mileage and 
successful completion of the code free from runtime errors or warnings. 
Provide a screenshot or screenshots so that the evaluator can check the 
mileage and that your code ran successfully to completion. The 
screenshot(s) should include a view of the console output, the project files, 
etc. The screenshot(s) can be added anywhere in your submission, e.g., the 
document, separately, in the project folder -but make it easy to find. 
I1: STRENGTHS OF THE CHOSEN ALGORITHM 
Identify at least two specific strengths of the algorithm from Part A relevant to 
finding a solution. 
Strengths can include anything, e.g., efficiency, simplicity, adaptability, etc. 
You also need to justify that these are strengths relative to the project. 
I2: VERIFICATION OF ALGORITHM
Verify that the algorithm used in the application meets all the requirements 
by: 
- Provide the total combined miles traveled by all trucks. It must be less 
than 140. 
- State that all packages were delivered on time. 
- State that all packages were delivered according to their delivery 
specifications. 
- Describe how all the above points are verifiable through the user 
interface. 
By “requirements,” they mean requirements of the solution -not requirements 
of the algorithm listed in Part A. Evaluators should be able to verify the 
mileage and deliveries via the user interface. So this section may seem a 
little odd as it equates verification with “stating,” but that is what they ask you 
to do. 
I3: OTHER POSSIBLE ALGORITHMS 
The submission identifies two algorithms different from the one provided in 
Part A that could meet the scenario’s requirements. 
The two alternative algorithms only need to be different from the algorithm 
identified in Part A; they do not need to be equitable or better in completelyknown. Furthermore, these two algorithms could apply to any portion of the 
application. The problem of finding a delivery route is known as the “Traveling 
Salesperson Problem” or TSP. An old and well-known problem, there are 
many, many approaches to this problem. 
I3A: ALGORITHM DIFFERENCES 
The description includes attributes of each algorithm identified in Part I3 and 
how the identified attributes compare to the algorithm’s attributes from Part 
A. 
Compare the two alternative algorithms to the algorithm identified in Part A. 
Attributes, and the comparison can include almost anything, e.g., timecomplexity, advantages, disadvantages, etc. The rubric writes 
“attribute-s.” So you should list at least two attributes per algorithm list in Part 
I3. 
J: DIFFERENT APPROACH 
The description includes at least one aspect of the process that the candidate 
would do differently and includes how the candidate would modify the 
process. 
K1: VERIFICATION OF DATA STRUCTURE
Verify that the data structure used in the application meets all the 
requirements by: 
- Provide the total combined miles traveled by all trucks. It must be less 
than 140. 
- State that all packages were delivered on time. 
- State that all packages were delivered according to their delivery 
specifications. 
- State that an “efficient” hash-table (Part D) with a look-up function (Part 
F) is present. 
- State that the “reporting” (package statuses and information) can be 
verified through the user interface and that all information is accurate 
(Part G). 
This section looks to have been cut and pasted from Part I2. It is confusing 
that you are asked to re-verify mileage and delivery statuses, particularly as 
these items are not relevant to the hash table. However, these items are 
specified in the rubric. When the rubric is redundant -be redundant. 
By “requirements,” they mean requirements of the solution -not requirements 
of the data structure listed in Part D. Evaluators should be able to verify the 
mileage and deliveries via the user interface. Other parts are addressed in 
previous sections. So this section is a little odd as it equates verification with 
“stating,” but that is what they ask you to do. 
K1A: EFFICIENCY 
The discussion accurately explains how adding packages directly affects the 
time needed to complete the look-up function.
The “look-up function” refers to the hash table’s look-up function identified in 
Part D. Describe how adding more packages affects the time it takes to 
retrieve package information. The effect could be nil, as in the case of a direct 
(1-1) mapping. Whatever the case, provide a brief explanation. 
K1B: OVERHEAD 
The discussion accurately explains how adding packages directly affects the 
data structure space usage. 
K1C: IMPLICATIONS 
The discussion accurately explains adding trucks or cities would affect lookup time and space usage. 
Look-up and space usage are both referring to the hash-table. Depending on 
your code, additional cities or trucks may not affect hash-table performance. 
In which case, you should explain why. 
K2: OTHER DATA STRUCTURES 
The submission identifies two data structures other than the one used in Part 
D to meet the requirements in the scenario. 
Identify two alternative data structures and justify why they could have been 
used as your hash-table. The alternatives can include modifications of the 
hash table listed in Part D. 
K2A: DATA STRUCTURES DIFFERENCES 
The submission accurately describes attributes of both data structures 
identified in part K2 and compares these to Part D’s data structure attributes. 
Attributes and the comparison can include almost anything, e.g., mappings, 
structure, advantages, disadvantages, etc. The rubric writes “attribute-s.” So 
you should list at least two attributes per data structure from part K2. 
L: SOURCES 
The submission includes in-text citations for properly quoted sources, 
paraphrased, or summarized and a reference list that accurately identifies 
the author, date, title, and source location as available.
You must follow (APA standards). Every reference listed must have a 
matching in-text citation; sources not warranting an in-text citation should be 
excluded. If you used no sources, include a sources section in your 
documentation stating “no outside sources were used.” You should include 
all code in code comments. Contact the writing center for questions or help 
with this portion. 
M: PROFESSIONAL COMMUNICATION 
The content reflects an attention to detail, is organized, and focuses on the 
main ideas as prescribed in the task or chosen by the candidate. Terminology 
is pertinent, is used correctly, and effectively conveys the intended meaning. 
Mechanics, usage, and grammar promote accurate interpretation and 
understanding. 
__________

[General FAQ]

Do all packages have to be delivered on time? 
Yes. Packages must be delivered on or before their delivery time. Packages 
labeled "EOD" must be delivered before the "End Of Day." "EOD" is not 
specified, but it's reasonable to assume that it's 5:00 pm. However, 
solutions almost always complete before 3:00 pm. 
Why are there three trucks? 
Only two drivers are available, and trucks have unlimited gas and load 
instantly. Perhaps, a third truck makes instantaneous load times realistic 
(truck three can be loaded while the others are out). However, it is not 
required to use truck 3 (or truck 1). 
What is the maximum total mileage allowed for trucks? 
Less than 140 miles. This is what the official task directions mean by 
"optimal." Both heuristics and optimizing algorithms are essential to get a 
good solution. 
Does the solution have to be optimal? 
The delivery problem is a variation of the traveling salesperson problem
(TSP) known as NP-Hard. Even if you found the optimal solution, we 
couldn't verify it without checking every possible route (and we don't have 
enough time for that!). Furthermore, the task requires your algorithm to be 
"efficient," meaning it must run in polynomial time. If you find a polynomialtime algorithm for solving the TSP, please let us know as this would answer 
the P versus NP problem -a millennium problem with a one million dollar 
prize. 
Therefore, you should use an algorithm that finds a solution and sufficient 
optimization. For this, many approaches will result in far less than 140 
miles. 
Do I need to use any algorithms not covered in the learning materials? 
No, but you certainly can. However, a program using only the covered 
algorithms (plus some heuristics) can find a solution. 
Can I use external third-party libraries? 
No. Only submit code that you've written yourself or from the standard builtin Python library. Evaluators will need to run your code on their machines 
without installing additional resources. 
Can I use the built-in Python dictionary construct for my hash table? 
No. Your hash table can use lists, sets, or tuples. You can use dictionaries 
elsewhere in your project. 
Does my program have to parse the excel data straight from excel? 
No. You can export the data from excel to text or CSV file. Include these 
files with your submitted project. You can clean up the file manually, making 
it easier to import, e.g., removing headers. 
The Excel mileage matrix has the lower half filled in, so it only has 
mileage entries in one direction, for example, from point A to point B, 
but not from point B to point A. Does that mean a truck has to find an 
alternate route? 
No. The distance table is bi-directional, i.e., the distance from A to B equals 
B to A. Furthermore, the distance table is a fully connected graph, i.e., it 
provides a direct path between every address. So using a graph data 
structure is not necessary. 
However, the triangle inequality does not hold. Meaning the provided 
distance from A to B mileage might not always be the shortest path! For 
example, from the distance table: hub-->Taylorsville is 11.0, but hub-> 
Valley Regional--> Taylorsville is 6.4+0.6 =7 miles. You can optimize the 
distance table via a pathfinding algorithm, such as Dijkstra's. However, this 
step is not necessary to find a solution under 140 miles. 
Does my program need to have an interactive external user interface? 
Yes. See Part G above. The 'user' needs to check the status of any 
package at any time conveniently. For example, the user should look up 
package #19 at 10:43 am and check the info and status. Having the user 
provide a time and printing the information and statuses of all the packages 
will meet this requirement. We recommend a simple command-line 
interface.
Does the user need to be able to update the package's address? 
There is no requirement for this, and the code should be able to complete 
the delivery simulation using only the provided data. 
How do we handle the package with the wrong address (#9)? 
The wrong delivery address for package #9, Third District Juvenile Court, will 
be corrected at 10:20 a.m. The correct address is “410 S State St., Salt Lake 
City, UT 84111”. There is no specification for handling this situation other than 
package #9 cannot be delivered to the correct address before 10:20 a.m. It 
is acceptable to assume WGUPS knows the address is incorrect and when 
it will be corrected. Hence effectively treating package #9 like a delayed 
package. 
How do we handle packages with the special notes: 
- Package #14: “Must be delivered with 15, 19.” 
- Package #16: “Must be delivered with 13, 19.” 
- Package #20: “Must be delivered with 13, 15.” 
- Packages #13, #14, #15. #16, #19, and #20 must go out for delivery 
on the same truck simultaneously, e.g., those packages all leave the 
hub at 9:30 on truck 2. 
Can I change the data files? 
Yes, you can make non-meaningful changes to WGUPS Distance Table.xlsx
and WGUPS Package
Table.xlsx. Don’t change the distances! But you may remove headers, 
change address formats, e.g., ‘S’ to 
‘South’, and convert the .xlsx files into a ‘.csv’ file (necessary for importing 
the data). 
Note: there is one minor differences between the addresses in the package 
and distance files: 
Distance file: 
5383 S 900 East 
#104 (84117) 
Package file: 
5383 South 900 
East #104

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<Copy of Raw Data From WGUPS_Package_File.csv file>

"Package
ID",Address,City,State,Zip,"Delivery
Deadline","Weight
KILO",Special Notes
1,195 W Oakland Ave,Salt Lake City,UT,84115,10:30 AM,21,
2,2530 S 500 E,Salt Lake City,UT,84106,EOD,44,
3,233 Canyon Rd,Salt Lake City,UT,84103,EOD,2,Can only be on truck 2
4,380 W 2880 S,Salt Lake City,UT,84115,EOD,4,
5,410 S State St,Salt Lake City,UT,84111,EOD,5,
6,3060 Lester St,West Valley City,UT,84119,10:30 AM,88,Delayed on flight---will not arrive to depot until 9:05 am
7,1330 2100 S,Salt Lake City,UT,84106,EOD,8,
8,300 State St,Salt Lake City,UT,84103,EOD,9,
9,300 State St,Salt Lake City,UT,84103,EOD,2,Wrong address listed
10,600 E 900 South,Salt Lake City,UT,84105,EOD,1,
11,2600 Taylorsville Blvd,Salt Lake City,UT,84118,EOD,1,
12,3575 W Valley Central Station bus Loop,West Valley City,UT,84119,EOD,1,
13,2010 W 500 S,Salt Lake City,UT,84104,10:30 AM,2,
14,4300 S 1300 E,Millcreek,UT,84117,10:30 AM,88,"Must be delivered with 15, 19"
15,4580 S 2300 E,Holladay,UT,84117,9:00 AM,4,
16,4580 S 2300 E,Holladay,UT,84117,10:30 AM,88,"Must be delivered with 13, 19"
17,3148 S 1100 W,Salt Lake City,UT,84119,EOD,2,
18,1488 4800 S,Salt Lake City,UT,84123,EOD,6,Can only be on truck 2
19,177 W Price Ave,Salt Lake City,UT,84115,EOD,37,
20,3595 Main St,Salt Lake City,UT,84115,10:30 AM,37,"Must be delivered with 13, 15"
21,3595 Main St,Salt Lake City,UT,84115,EOD,3,
22,6351 South 900 East,Murray,UT,84121,EOD,2,
23,5100 South 2700 West,Salt Lake City,UT,84118,EOD,5,
24,5025 State St,Murray,UT,84107,EOD,7,
25,5383 South 900 East #104,Salt Lake City,UT,84117,10:30 AM,7,Delayed on flight---will not arrive to depot until 9:05 am
26,5383 South 900 East #104,Salt Lake City,UT,84117,EOD,25,
27,1060 Dalton Ave S,Salt Lake City,UT,84104,EOD,5,
28,2835 Main St,Salt Lake City,UT,84115,EOD,7,Delayed on flight---will not arrive to depot until 9:05 am
29,1330 2100 S,Salt Lake City,UT,84106,10:30 AM,2,
30,300 State St,Salt Lake City,UT,84103,10:30 AM,1,
31,3365 S 900 W,Salt Lake City,UT,84119,10:30 AM,1,
32,3365 S 900 W,Salt Lake City,UT,84119,EOD,1,Delayed on flight---will not arrive to depot until 9:05 am
33,2530 S 500 E,Salt Lake City,UT,84106,EOD,1,
34,4580 S 2300 E,Holladay,UT,84117,10:30 AM,2,
35,1060 Dalton Ave S,Salt Lake City,UT,84104,EOD,88,
36,2300 Parkway Blvd,West Valley City,UT,84119,EOD,88,Can only be on truck 2
37,410 S State St,Salt Lake City,UT,84111,10:30 AM,2,
38,410 S State St,Salt Lake City,UT,84111,EOD,9,Can only be on truck 2
39,2010 W 500 S,Salt Lake City,UT,84104,EOD,9,
40,380 W 2880 S,Salt Lake City,UT,84115,10:30 AM,45,

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<Copy of Raw Data From WGUPS_Distance_Table.csv file>

DISTANCE BETWEEN HUBS IN MILES,,"Western Governors University
4001 South 700 East, 
Salt Lake City, UT 84107","International Peace Gardens
 1060 Dalton Ave S","Sugar House Park
 1330 2100 S","Taylorsville-Bennion Heritage City Gov Off
 1488 4800 S","Salt Lake City Division of Health Services 
 177 W Price Ave","South Salt Lake Public Works
 195 W Oakland Ave","Salt Lake City Streets and Sanitation
 2010 W 500 S","Deker Lake
 2300 Parkway Blvd","Salt Lake City Ottinger Hall
 233 Canyon Rd","Columbus Library
 2530 S 500 E","Taylorsville City Hall
 2600 Taylorsville Blvd","South Salt Lake Police
 2835 Main St","Council Hall
 300 State St","Redwood Park
 3060 Lester St","Salt Lake County Mental Health
 3148 S 1100 W","Salt Lake County/United Police Dept
 3365 S 900 W","West Valley Prosecutor
 3575 W Valley Central Sta bus Loop","Housing Auth. of Salt Lake County
 3595 Main St","Utah DMV Administrative Office
 380 W 2880 S","Third District Juvenile Court
 410 S State St","Cottonwood Regional Softball Complex
 4300 S 1300 E","Holiday City Office
 4580 S 2300 E","Murray City Museum
 5025 State St","Valley Regional Softball Complex
 5100 South 2700 West","City Center of Rock Springs
 5383 South 900 East #104","Rice Terrace Pavilion Park
 600 E 900 South","Wheeler Historic Farm 
 6351 South 900 East"
"Western Governors University
4001 South 700 East, 
Salt Lake City, UT 84107",HUB,0,,,,,,,,,,,,,,,,,,,,,,,,,,
"International Peace Gardens
 1060 Dalton Ave S","1060 Dalton Ave S
(84104)",7.2,0,,,,,,,,,,,,,,,,,,,,,,,,,
"Sugar House Park
 1330 2100 S","1330 2100 S
(84106)",3.8,7.1,0,,,,,,,,,,,,,,,,,,,,,,,,
"Taylorsville-Bennion Heritage City Gov Off
 1488 4800 S","1488 4800 S
(84123)",11,6.4,9.2,0,,,,,,,,,,,,,,,,,,,,,,,
"Salt Lake City Division of Health Services 
 177 W Price Ave","177 W Price Ave
(84115)",2.2,6,4.4,5.6,0,,,,,,,,,,,,,,,,,,,,,,
"South Salt Lake Public Works
 195 W Oakland Ave","195 W Oakland Ave
(84115)",3.5,4.8,2.8,6.9,1.9,0,,,,,,,,,,,,,,,,,,,,,
"Salt Lake City Streets and Sanitation
 2010 W 500 S","2010 W 500 S
(84104)",10.9,1.6,8.6,8.6,7.9,6.3,0,,,,,,,,,,,,,,,,,,,,
"Deker Lake
 2300 Parkway Blvd","2300 Parkway Blvd
(84119)",8.6,2.8,6.3,4,5.1,4.3,4,0,,,,,,,,,,,,,,,,,,,
"Salt Lake City Ottinger Hall
 233 Canyon Rd","233 Canyon Rd
(84103)",7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0,,,,,,,,,,,,,,,,,,
"Columbus Library
 2530 S 500 E","2530 S 500 E
(84106)",2.8,6.3,1.6,7.3,2.6,1.5,8,9.3,4.8,0,,,,,,,,,,,,,,,,,
"Taylorsville City Hall
 2600 Taylorsville Blvd","2600 Taylorsville Blvd
(84118)",6.4,7.3,10.4,1,6.5,8.7,8.6,4.6,11.9,9.4,0,,,,,,,,,,,,,,,,
"South Salt Lake Police
 2835 Main St","2835 Main St
(84115)",3.2,5.3,3,6.4,1.5,0.8,6.9,4.8,4.7,1.1,7.3,0,,,,,,,,,,,,,,,
"Council Hall
 300 State St","300 State St
(84103)",7.6,4.8,5.3,11.1,7.5,4.5,4.2,7.7,0.6,5.1,12,4.7,0,,,,,,,,,,,,,,
"Redwood Park
 3060 Lester St","3060 Lester St
(84119)",5.2,3,6.5,3.9,3.2,3.9,4.2,1.6,7.6,4.6,4.9,3.5,7.3,0,,,,,,,,,,,,,
"Salt Lake County Mental Health
 3148 S 1100 W","3148 S 1100 W
(84119)",4.4,4.6,5.6,4.3,2.4,3,8,3.3,7.8,3.7,5.2,2.6,7.8,1.3,0,,,,,,,,,,,,
"Salt Lake County/United Police Dept
 3365 S 900 W","3365 S 900 W
(84119)",3.661128164,4.5,5.8,4.4,2.7,3.8,5.8,3.4,6.6,4,5.4,2.9,6.6,1.5,0.6,0,,,,,,,,,,,
"West Valley Prosecutor
 3575 W Valley Central Sta bus Loop","3575 W Valley Central Station bus Loop
(84119)",7.6,7.4,5.7,7.2,1.4,5.7,7.2,3.1,7.2,6.7,8.1,6.3,7.2,4,6.4,5.6,0,,,,,,,,,,
"Housing Auth. of Salt Lake County
 3595 Main St","3595 Main St
(84115)",2,6,4.1,5.3,0.5,1.9,7.7,5.1,5.9,2.3,6.2,1.2,5.9,3.2,2.4,1.6,7.1,0,,,,,,,,,
"Utah DMV Administrative Office
 380 W 2880 S","380 W 2880 S
(84115)",3.6,5,3.6,6,1.7,1.1,6.6,4.6,5.4,1.8,6.9,1,5.4,3,2.2,1.7,6.1,1.6,0,,,,,,,,
"Third District Juvenile Court
 410 S State St","410 S State St
(84111)",6.5,4.8,4.3,10.6,6.5,3.5,3.2,6.7,1,4.1,11.5,3.7,1,6.9,6.8,6.4,7.2,4.9,4.4,0,,,,,,,
"Cottonwood Regional Softball Complex
 4300 S 1300 E","4300 S 1300 E
(84117)",1.9,9.5,3.3,5.9,3.2,4.9,11.2,8.1,8.5,3.8,6.9,4.1,8.5,6.2,5.3,4.9,10.6,3,4.6,7.5,0,,,,,,
"Holiday City Office
 4580 S 2300 E","4580 S 2300 E
(84117)",3.4,10.9,5,7.4,5.2,6.9,12.7,10.4,10.3,5.8,8.3,6.2,10.3,8.2,7.4,6.9,12,5,6.6,9.3,2,0,,,,,
"Murray City Museum
 5025 State St","5025 State St
(84107)",2.4,8.3,6.1,4.7,2.5,4.2,10,7.8,7.8,4.3,4.1,3.4,7.8,5.5,4.6,4.2,9.4,2.3,3.9,6.8,2.9,4.4,0,,,,
"Valley Regional Softball Complex
 5100 South 2700 West","5100 South 2700 West
(84118)",6.4,6.9,9.7,0.6,6,9,8.2,4.2,11.5,7.8,0.4,6.9,11.5,4.4,4.8,5.6,7.5,5.5,6.5,11.4,6.4,7.9,4.5,0,,,
"City Center of Rock Springs
 5383 South 900 East #104","5383 S 900 East #104
(84117)",2.4,10,6.1,6.4,4.2,5.9,11.7,9.5,9.5,4.8,4.9,5.2,9.5,7.2,6.3,5.9,11.1,4,5.6,8.5,2.8,3.4,1.7,5.4,0,,
"Rice Terrace Pavilion Park
 600 E 900 South","600 E 900 South
(84105)",5,4.4,2.8,10.1,5.4,3.5,5.1,6.2,2.8,3.2,11,3.7,2.8,6.4,6.5,5.7,6.2,5.1,4.3,1.8,6,7.9,6.8,10.6,7,0,
"Wheeler Historic Farm 
 6351 South 900 East","6351 South 900 East
(84121)",3.6,13,7.4,10.1,5.5,7.2,14.2,10.7,14.1,6,6.8,6.4,14.1,10.5,8.8,8.4,13.6,5.2,6.9,13.1,4.1,4.7,3.1,7.8,1.3,8.3,0

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

<List of addresses shown on the Salt Lake City - Downtown Map png image they want you to reference to get those locations for the project>
<Having the actual image/png shouldn't actually be needed anymore now that the complete, accurate, raw data is available here>

0,Western Governors University,4001 South 700 East
1,International Peace Gardens,1060 Dalton Ave S
2,Sugar House Park,1330 2100 S
3,Taylorsville-Bennion Heritage City Gov Off,1488 4800 S
4,Salt Lake City Division of Health Services,177 W Price Ave
5,South Salt Lake Public Works,195 W Oakland Ave
6,Salt Lake City Streets and Sanitation,2010 W 500 S
7,Deker Lake,2300 Parkway Blvd
8,Salt Lake City Ottinger Hall,233 Canyon Rd
9,Columbus Library,2530 S 500 E
10,Taylorsville City Hall,2600 Taylorsville Blvd
11,South Salt Lake Police,2835 Main St
12,Council Hall,300 State St
13,Redwood Park,3060 Lester St
14,Salt Lake County Mental Health,3148 S 1100 W
15,Salt Lake County United Police Dept,3365 S 900 W
16,West Valley Prosecutor,3575 W Valley Central Station bus Loop
17,Housing Auth. of Salt Lake County,3595 Main St
18,Utah DMV Administrative Office,380 W 2880 S
19,Third District Juvenile Court,410 S State St
20,Cottonwood Regional Softball Complex,4300 S 1300 E
21,Holiday City Office,4580 S 2300 E
22,Murray City Museum,5025 State St
23,Valley Regional Softball Complex,5100 South 2700 West
24,City Center of Rock Springs,5383 South 900 East #104
25,Rice Terrace Pavilion Park,600 E 900 South
26,Wheeler Historic Farm,6351 South 900 East

______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________