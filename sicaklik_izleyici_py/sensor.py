import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorNode(Node):

  def __init__(self):
    super().__init__('sensor')
    self.publisher_ = self.create_publisher(Float32, 'sicaklik', 10)
    self.timer = self.create_timer(1.0, self.timer_callback)

  def timer_callback(self):
    msg = Float32()
    # 20 ile 40 arasında rastgele sıcaklık üretilir
    msg.data = round(random.uniform(20.0, 40.0), 2)
    self.publisher_.publish(msg)
    self.get_logger().info(f'Yayınlanan Sıcaklık: {msg.data}')


def main(args=None):
  rclpy.init(args=args)
  sensor_node = SensorNode()
  rclpy.spin(sensor_node)
  sensor_node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()
