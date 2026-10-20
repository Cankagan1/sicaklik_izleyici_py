import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class IzleyiciNode(Node):

  def __init__(self):
    super().__init__('izleyici')

    # Bonus: Eşik değerini declare_parameter ile tanımlıyoruz (varsayılan: 30.0)
    self.declare_parameter('esik_deger', 30.0)
    self.esik = (
        self.get_parameter('esik_deger').get_parameter_value().double_value
    )

    self.subscription = self.create_subscription(
        Float32, 'sicaklik', self.listener_callback, 10
    )
    self.get_logger().info(f'İzleyici başlatıldı. Eşik değer: {self.esik}')

  def listener_callback(self, msg):
    sicaklik = msg.data
    self.get_logger().info(f'Gelen Sıcaklık: {sicaklik}')

    # Değer belirlenen eşik üzerindeyse uyarı ver
    if sicaklik > self.esik:
      self.get_logger().warn(
          f'DİKKAT! Sıcaklık yüksek: {sicaklik} (Eşik: {self.esik})'
      )


def main(args=None):
  rclpy.init(args=args)
  izleyici_node = IzleyiciNode()
  rclpy.spin(izleyici_node)
  izleyici_node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()
