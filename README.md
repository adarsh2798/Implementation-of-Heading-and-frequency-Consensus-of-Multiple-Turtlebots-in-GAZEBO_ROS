# Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS

In this project, Consensus of multi-agent system is implemenetd. A multiagent system (MAS) can be reprsented by a graph, with a set of nodes (reprsenting the agents) and edges (reprsents the information exchange between agents). By analyzing the Laplacian and adjacency matrices of the underlying graph, various control laws can be developed and their convergence can be proved.

Consensus means when all the states of all the agents converge to same values. In this project, Heading and frequency consensus is implemented. 4 turtlebots were used in GAZEBO. A simple undirected underlying graph was used. 4 separate python scripts were used for each turtlebot/Node in the MAS graph. Each turtlebot subscibed to it's neighbor's /odom topic.

To see full details about this implemenation see the [report](https://github.com/adarsh2798/Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS/blob/main/assignment3/sc627_assignmnt3.pdf)

## 1. SIMULATION RESULTS OF HEADING CONSENSUS

Here one can clearly see all the 4 turtlebots converge to same heading.

<p align="center">
  <img src="https://github.com/adarsh2798/Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS/blob/main/assignment3/simulation_results/consensus_proper.png" />
</p>

![Alt Text](https://github.com/adarsh2798/Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS/blob/main/assignment3/simulation_results/consesnus_heading_1.gif)

## 1. SIMULATION RESULTS OF FREQUENCY CONSENSUS

Here, all the 4 turtlebots converge to same heading and further rotate with same angualar velocity there onwards. The 1st figure below shows teh convergence of angualar velocity to same value. The 2nd image shows the heading of 4 turtlebots. One can see eventually they converge and vary together.
<p align="center">
  <img src="https://github.com/adarsh2798/Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS/blob/main/assignment3/simulation_results/freq_sync_w.png" />
</p>

<p align="center">
  <img src="https://github.com/adarsh2798/Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS/blob/main/assignment3/simulation_results/freq_sync.png" />
</p>

![Alt Text](https://github.com/adarsh2798/Implementation-of-Heading-and-frequency-Consensus-of-Multiple-Turtlebots-in-GAZEBO_ROS/blob/main/assignment3/simulation_results/freq_sync.gif)
