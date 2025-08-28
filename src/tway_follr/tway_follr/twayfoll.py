import sys
import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TheWayfollw(Node):
    def __init__(self):
        super().__init__('TheWayFollowingRobot')
        self.publisher = self.create_publisher(Twist,
                                               '/turtle1/cmd_vel',
                                               10)
        self.subscription = self.create_subscription(Pose,
                                                     '/turtle1/pose',
                                                     self.pose_callback,
                                                     10)
        self.pose = None

        if len(sys.argv) < 4:
            self.get_logger().error("Usage: ros2 run tway_follr tway_follr_node <x> <y> <theta>")
            sys.exit(1)

        self.x2 = float(sys.argv[1]); self.y2 = float(sys.argv[2]); self.theta = float(sys.argv[3])

    def pose_callback(self, msg):
        self.pose = msg

        d = math.sqrt((self.x2- self.pose.x)**2 + (self.y2 - self.pose.y)**2)
        angle = math.atan2(self.y2 - self.pose.y, self.x2 - self.pose.x)

        angle_diff = angle - self.pose.theta

        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi

        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi

        twist = Twist()

        if abs(angle_diff) > 0.1:
            twist.angular.z = 2.0 * angle_diff
        elif d > 0.1:
            twist.linear.x = 2.0 * d
        else:
            self.get_logger().info(f"Reached target ({self.x2}, {self.y2}). Traveled: {d:.2f} units")
            twist.linear.x = 0.0 ; twist.angular.z = 0.0

        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = TheWayfollw()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
