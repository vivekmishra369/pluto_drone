#!/home/gaia/miniconda3/bin/python
import rospy 
import sys 
import cv2 as cv
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
import numpy as np
import matplotlib.pyplot as plt


# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.shape)
def show_img_cb(frame):

    try: 
        cv.namedWindow("RGB_Image", cv.WINDOW_NORMAL)
        # cv.moveWindow("RGB_Image", 25, 75)
        
        

        cv.imshow("RGB_Image",frame)
        cv.waitKey(3)
    except Exception as e:
        print(e)

def image_callback(ros_image):
    # Use cv_bridge() to convert the ROS image to OpenCV format
    # try:
    #     bridge = CvBridge()
    #     frame = bridge.imgmsg_to_cv2(ros_image, "bgr8")
        
    # except CvBridgeError as  e:
    #     print(e)
    #     pass

    # # Convert the image to a Numpy array since most cv2 functions
    # # require Numpy arrays.
    # frame = np.array(frame, dtype=np.uint8)
    # bridge = CvBridge()
    # cvimage = bridge.imgmsg_to_cv2(ros_image, desired_encoding='passthrough')
    frame = np.frombuffer(ros_image.data, dtype=np.uint8).reshape(ros_image.height, ros_image.width, -1)
    print(frame.shape, ros_image.height,ros_image.width)
    # cv.imwrite("test.png",frame)
    # rospy.Timer(rospy.Duration(0.03), show_img_cb)


    try: 
        cv.namedWindow("RGB_Image", cv.WINDOW_NORMAL)
        # cv.moveWindow("RGB_Image", 25, 75)
        
        

        cv.imshow("RGB_Image",frame)
        cv.waitKey(3)
    except Exception as e:
        print(e)
    # Process the frame using the process_image() function
    # self.display_image = self.process_image(frame)

def simple():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('simple', anonymous=True)

    rospy.Subscriber("/plutocamera/image_raw", Image, image_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    simple()