# Sıcaklık İzleyici (ROS 2 Python Paketi)

Bu proje, ROS 2 kullanarak rastgele sıcaklık üreten bir sensör düğümü ile bu sıcaklığı takip eden ve eşik değerine göre uyarı veren bir izleyici düğümünü içermektedir.

## Proje İçeriği
- **`sensor.py`**: Her saniye 20-40 arasında rastgele sıcaklık değeri üretir ve `/sicaklik` konusuna `Float32` türünde yayınlar.
- **`izleyici.py`**: `/sicaklik` konusunu dinler, değeri ekrana yazdırır ve değer belirlenen eşik değerinin (varsayılan: 30) üzerindeyse `get_logger().warn()` ile uyarı verir.

## Çalıştırma Adımları

1. **Paketi Çalışma Alanına (Workspace) Kopyalayın:**
   Paket klasörünü ROS 2 çalışma alanınızın `src` dizini altına yerleştirin (`~/ros2_ws/src/sicaklik_izleyici_py`).

2. **Projeyi Derleyin:**
   Çalışma alanınızın ana dizinine gelerek projeyi derleyin:
   bash
   cd ~/ros2_ws
   colcon build --packages-select sicaklik_izleyici_py
