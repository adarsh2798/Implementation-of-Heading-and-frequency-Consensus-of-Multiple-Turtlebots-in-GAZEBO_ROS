#!/usr/bin/env python3

import rospy
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
#from kobuki_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from std_msgs.msg import Float64MultiArray
import matplotlib.pyplot as plt
import time
s=0
e=0
yaw1=0
yaw2=0
yaw3=0
yaw4=0
y1=[]
y2=[]
y3=[]
y4=[]
s=time.time()
def odom_callback_1(msg):
     global yaw1,yaw2,yaw3,yaw4
     global flag_laser
     global arg
    
     ori=msg.pose.pose.orientation
     pos=msg.pose.pose.position
     oril=[ori.x,ori.y,ori.z,ori.w]
     yaw1=euler_from_quaternion(oril)[2]
     loc1=np.array([[pos.x],[pos.y]])
        
def odom_callback_2(msg):
     global yaw1,yaw2,yaw3,yaw4
     global flag_laser
     global arg
    
     ori=msg.pose.pose.orientation
     pos=msg.pose.pose.position
     oril=[ori.x,ori.y,ori.z,ori.w]
     yaw2=euler_from_quaternion(oril)[2]
     loc2=np.array([[pos.x],[pos.y]])
        
def odom_callback_3(msg):
     global yaw1,yaw2,yaw3,yaw4
     global flag_laser
     global arg
    
     ori=msg.pose.pose.orientation
     pos=msg.pose.pose.position
     oril=[ori.x,ori.y,ori.z,ori.w]
     yaw3=euler_from_quaternion(oril)[2]
     loc3=np.array([[pos.x],[pos.y]])
            
def odom_callback_4(msg):
     global yaw1,yaw2,yaw3,yaw4
     global flag_laser
     global arg
    
     ori=msg.pose.pose.orientation
     pos=msg.pose.pose.position
     oril=[ori.x,ori.y,ori.z,ori.w]
     yaw4=euler_from_quaternion(oril)[2]
     loc4=np.array([[pos.x],[pos.y]])
        
def laplacian_publisher():
    global s,e
    global yaw1,yaw2,yaw3,yaw4,y1,y2,y3,y4
    
   
    rospy.init_node('laplacian_adjacency_publisher', anonymous=True)

    
    num_nodes = 4
   
    adjacency = np.array([[0, 1.5, 0, 0],
                             [1.5, 0, 1.5, 1.5*(2**0.5)],
                             [0, 1.5, 0, 1.5],
                             [0, 1.5*(2**0.5), 1.5, 0]])
    
    
   
    # Compute the Laplacian matrix
    laplacian = np.diag(np.sum(adjacency, axis=1)) - adjacency

    # Create the publisher for the Laplacian matrix
    pub = rospy.Publisher('laplacian_adjacency_matrix', Float64MultiArray, queue_size=10)

    # Initialize the rate at which to publish messages
    rate = rospy.Rate(10) # 10 Hz

    # Loop until the node is shutdown
    while not rospy.is_shutdown():
        # Create the message to publish
        msg = Float64MultiArray()
        msg.data = laplacian.flatten()

        # Publish the message
        pub.publish(msg)
        
        
        subscribe_to_odometry1=rospy.Subscriber('bot_1/odom', Odometry, callback = odom_callback_1)
        subscribe_to_odometry2=rospy.Subscriber('bot_2/odom', Odometry, callback = odom_callback_2)
        subscribe_to_odometry3=rospy.Subscriber('bot_3/odom', Odometry, callback = odom_callback_3)
        subscribe_to_odometry4=rospy.Subscriber('bot_4/odom', Odometry, callback = odom_callback_4)
        y1.append(yaw1)
        y2.append(yaw2)
        y3.append(yaw3)
        y4.append(yaw4)
        m=np.mean([yaw1,yaw2,yaw3,yaw4])
        sd=np.std([yaw1,yaw2,yaw3,yaw4])
        print(sd)
        if sd<1e-3 and yaw1!=0 and yaw2!=0 and yaw3!=0 and yaw4!=0:
            e=time.time()
            diff=e-s
            tt=np.linspace(0,diff,len(y1[1:]))
            
            plt.plot(tt,np.array(y1[1:]),'blue')
            plt.plot(tt,np.array(y2[1:]),'green')
            plt.plot(tt,np.array(y3[1:]),'red')
            plt.plot(tt,np.array(y4[1:]),'magenta')
            plt.legend(["heading-1", "heading-2","heading-3","heading-4"], loc ="lower right")
            plt.xlabel('time(s)')
            plt.ylabel('radians')
            plt.show()
        # Sleep to maintain the desired publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        laplacian_publisher()

    except rospy.ROSInterruptException:
        pass

