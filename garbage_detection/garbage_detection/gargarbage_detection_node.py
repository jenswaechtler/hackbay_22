import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class GarbageDetection(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.imageCallback,
            10)

        self.subscription  # prevent unused variable warning

    def imageCallback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = GarbageDetection()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()