#!/usr/bin/env python3

import rospy 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
#from kobuki_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import matplotlib.pyplot as plt
import math
import numpy as np
import message_filters
from std_msgs.msg import Float64MultiArray
yaw1=0
yaw2=0
yaw3=0
yaw4=0
L=np.zeros((4,4))
def algo(yaw1,yaw2,yaw3,yaw4,L):
    
    y=np.array([yaw1,yaw2,yaw3,yaw4])

    w=-np.sum(np.multiply(L[1,:],y))
    move_the_bot.angular.z=w
    move_the_bot.linear.x=0
    publish_to_cmd_vel.publish(move_the_bot) 
    print("yaw2=",yaw2)

    

      

    


    
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
        
     algo(yaw1,yaw2,yaw3,yaw4,L) 
           
def L_A(msg):
       global L
       L = np.reshape(msg.data, (4, 4))        



if __name__ == "__main__":
    
    rospy.init_node('bot_2')
    
    r=rospy.Rate(10)
    subscribe_to_L_A=rospy.Subscriber('laplacian_adjacency_matrix', Float64MultiArray, callback = L_A)
    subscribe_to_odometry1=rospy.Subscriber('bot_1/odom', Odometry, callback = odom_callback_1)
    subscribe_to_odometry2=rospy.Subscriber('bot_2/odom', Odometry, callback = odom_callback_2)
    subscribe_to_odometry3=rospy.Subscriber('bot_3/odom', Odometry, callback = odom_callback_3)
    subscribe_to_odometry4=rospy.Subscriber('bot_4/odom', Odometry, callback = odom_callback_4)
    
    rospy.loginfo('My node has been started')
    publish_to_cmd_vel = rospy.Publisher('bot_2/cmd_vel', Twist, queue_size = 10)
    
  
    #create an object of Twist data

    move_the_bot = Twist()
    r.sleep()
    rospy.spin()


