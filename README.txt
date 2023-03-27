Name: Aiden Nelson
EID: 800742353
Date of Last Edit: 3/22/2023

--Built for CS340--

This project is a shortest path finder program that utilizes 3 
different graph algorithms to find the shortest path between a 
source and destination node input by the user (built from a 
'.txt' input file).

-----------------------------------------------------------------

To begin this program, place it in the folder with the graph files
that you would like to run it on. Be sure that it is in the exact
same folder/directory as the .txt files.

Then, simply navigate to that folder in the command line and run 
    python shortestPathProject.py

-----------------------------------------------------------------

By running the above command, you should be guided through the
process by the outputs (in the command line), but a brief guide
is provided below:

The project will first ask you about what input file you want to
use for this program. Simply enter the number next to the file that you 
want to choose, then press enter.

-----------------------------------------------------------------

After this, enter the source node that you would like to run the
graph algorithms from, and press enter. 

Then, you can pick any node that is in the graph (other than source)
to be the destination node (then press enter).

-----------------------------------------------------------------

Next, the program will determine the ideal graph algorithm to use,
either DAG Shortest Path, Dijkstra's, and Bellman-Ford (in that order)

Then, it will display the shortest path to that node and the distance to it.

-----------------------------------------------------------------

IF the algorithms run into any issues, (ie: negative edge weight cycle)
the output will tell you so, and it will exit or complete depending upon 
which issues your graph has.

-----------------------------------------------------------------

After the first destination's shortest path is calculated, you can enter
either 'y' or 'n' to enter another new destination node.

-----------------------------------------------------------------

If you entered 'n', you can now choose from the same two options as to if
you would like to enter another source node.

-----------------------------------------------------------------

Depending upon your selection, the program repeats itself. 

-----------------------------------------------------------------

Thank you for trying out the program, I hope everything works well!
May God bless.
