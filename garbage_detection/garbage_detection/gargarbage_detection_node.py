import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge, CvBridgeError


class GarbageDetection(Node):

    def __init__(self):
        super().__init__('garbage_detection_node')
        
        # TODO: change to msg_image and change topic
        self.subscription = self.create_subscription(
            Image,
            'image',
            self.imageCallback,
            10)

        self.subscription  # prevent unused variable warning

    def imageCallback(self, img_msg):
        # self.get_logger().info('I heard: "%s"' % msg.data)
        self.get_logger().info('Image received ')
        
        # Do all the magic here
        
        # 1. Ros image to openCV image
        try:
            bridge = CvBridge()
            cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
            cv_image = cv2.transpose(cv_image)
            cv_image = cv2.flip(cv_image, 1)
            self.show_image(cv_image)
        
        except CvBridgeError as e:
            rclpy.logerr("CvBridge Error: {0}".format(e))
        
        
        # 2. Garbage detection (open CV stuff -> bounding box)


        # 3. Publish video as youtube stream
        #
    
    def show_image(self, img):
        cv2.imshow("Image Window", img)
        cv2.waitKey(3)


def main(args=None):
    rclpy.init(args=args)

    node = GarbageDetection()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
