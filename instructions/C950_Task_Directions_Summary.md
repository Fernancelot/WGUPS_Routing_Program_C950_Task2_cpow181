C950 Task Directions and Rubric Summary

Alternative task directions and FAQ

Scenario

The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day; each package has specific criteria and delivery requirements.

Your task is to write code that determines and presents a solution delivering all 40 packages, listed in the attached "WGUPS Package File," on time, according to their criteria while reducing the total number of miles traveled by the trucks. The "Salt Lake City Downtown Map" provides each address's location, and the "WGUPS Distance Table" provides the distance between each address (note: mileage on the distance files may not match distances on the map).

The supervisor (user) needs the means to check the status of any given package at any given time using package IDs. The report should also include the delivery times, which packages are at the hub, and en route. The intent is to use this program for this specific location and use the same program in different cities as WGUPS expands its business. As such, you will need to include detailed comments following the industry-standards to make your code easy to read and justifying the decisions you made while writing your program.

Project Summary

You will write a program in Python, which does the following:

Can store the package information into a hash table.

Uses a self-adjusting heuristic algorithm to find a solution that delivers all packages using under 140 miles and according to the provided requirements (e.g., delivery deadlines, addresses, number of trucks, special notes, etc.).

Note: Non-self-adjusting methods are also allowed, but there must be at least one part that uses a self-adjusting algorithm (identified in Part A) with one scalable element (discussed in Part B4).

Allows the 'user' to check the status (at the hub, en route, or delivery time) of any package at any given time.

Using code comments and a separate document, complete the following:

Provide code comments for every significant portion of code that explains the logic and time complexity.

Provide documentation on algorithms used, alternative methods to, efficiency, and scalability of the methods used to find a solution.

Provide documentation on the data structure(s) describing their use, alternative methods, efficiency, and scalability of data processes.

Technical Requirements and Resources

Evaluators need to successfully run your code using only submitted files and the most recent version of Python. Submitted code may use anything from Python’s standard library, including the built-in data structures (e.g., lists, tuples, sets, and dictionaries), except for the hash table where only the use of dictionaries is prohibited.

The project must use the package and distance data provided in files WGUPS Distance Table.xlsx and WGUPS Package Table.xlsx found in View Task>Task Overview>Supporting Documents on the C950 COS page. You may make minor changes (such as removing headers) and convert these documents into .csv. files.

Note: There are minor differences between the addresses in the package and distance files:

Distance file: 5383 S 900 East #104 (84117)

Package file: 5383 South 900 East #104

Submitted code may use anything from Python’s standard library, including the built-in data structures (e.g., lists, tuples, sets, and dictionaries). The only exception is the hash-table, where the use of dictionaries is prohibited (a dictionary is a hash-table).

Assumptions

Two drivers and two trucks are available.

The trucks move at a constant speed of 18 miles per hour.

Trucks can carry a maximum of 16 packages.

Trucks can leave the hub no sooner than 8:00 a.m.

Trucks can be loaded only at the hub.

You only need to account for the time spent driving. You can ignore the time spent on all other activities, such as loading trucks and dropping off packages.

The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is “410 S State St., Salt Lake City, UT 84111”. You may assume that WGUPS knows the address is correct and when the correction will be available.

Packages #13, #14, #15, #16, #19, and #20 must go out for delivery on the same truck.

Packages #3, #18, #36, and #38 may only be delivered by truck 2.

Packages #6, #25, #28, and #32 cannot leave the hub before 9:05 a.m.

Rubric Requirements Summary

A: Algorithm Selection

Identify by name the self-adjusting algorithm used to create a program to deliver the packages and meet all requirements specified in the scenario.

B: Code Documentation

Provide pseudocode explaining the algorithm’s logic.

Describe the development environment.

Explain space-time complexity with Big-O notation.

Discuss adaptability and software maintainability.

C: Original Code

Ensure the code is original and runs without errors.

Include identification information in main.py.

D: Data Structure

Implement a self-adjusting hash table for package storage.

E & F: Hash Table Functions

Insert all package info.

Retrieve package info by ID.

G: User Interface

Provide an intuitive interface for checking package statuses and total mileage.

H: Proof of Code Execution

Show screenshots of successful code execution and total mileage.

I: Verification

Validate that all requirements are met and verifiable via the interface.

J: Process Improvements

Discuss possible improvements.

K: Data Structure Verification

Confirm hash table functionality and performance.

L: Sources

Use proper APA citations if applicable.

M: Professional Communication

Ensure grammar, clarity, and professional presentation.