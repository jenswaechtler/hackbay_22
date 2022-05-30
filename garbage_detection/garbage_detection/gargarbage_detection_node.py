import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class GarbageDetection(Node):

    def __init__(self):
        super().__init__('garbage_detection_node')
        
        # TODO: change to msg_image and change topic
        self.subscription = self.create_subscription(
            String,
            'image',
            self.imageCallback,
            10)

        self.subscription  # prevent unused variable warning

    def imageCallback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        
        # Do all the magic here
        #
        # 1. Ros image to openCV image
        # 2. Garbage detection (open CV stuff -> bounding box)
        # 3. Publish video as youtube stream
        #


def main(args=None):
    rclpy.init(args=args)

    node = GarbageDetection()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
