There are 2 directories: balanced_consensus which performs heading consensus and synchronization, which performs angular velocity synchronization
Each directory has 5 scripts: 4 for 4 turtlebots and one script for publishinh laplacian/adjacency to all 4 turtlebot nodes. Each turtlebot node subscribes to odometry topic of only it's neighbors,
To run, use :"roslaunch assignment3 consensus.launch"  OR "roslaunch assignment3 sync.launch" for consensus and synchronization repectively.


