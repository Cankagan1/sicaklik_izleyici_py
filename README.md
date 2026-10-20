# ROS 2 Sıcaklık İzleyici Projesi (Temperature Tracker)

Bu proje, Robot Operating System 2 (ROS 2) altyapısı kullanılarak geliştirilmiş, düğümler arası haberleşmeyi (pub-sub mimarisi) ve parametre yönetimini içeren uçtan uca bir sıcaklık takip sistemidir. Bu belgede sistemin mimarisi, tasarım kararları ve kodların detaylı mantığı açıklanmıştır.

---

## Projenin Amacı ve Mimari Tasarım Kararları

Dağıtık robotik sistemlerde sensör verilerinin okunması, işlenmesi ve kritik durumlarda uyarı mekanizmalarının tetiklenmesi temel bir gereksinimdir. Bu ödev kapsamında:
* **`rclpy` (ROS 2 Python Client Library)** kullanılarak Python tabanlı düğümler oluşturulmuştur.
* Veri paylaşımı için **Publish-Subscribe (Yayıncı-Abone)** modeli seçilmiştir. Böylece veri üreten kaynak (`sensor.py`) ile veriyi işleyen hedef (`izleyici.py`) birbirinden bağımsız bir şekilde haberleşir.

---

## Kod Bloklarının Detaylı Açıklamaları

### 1. `sensor.py` (Veri Üretici Düğüm) Neden ve Nasıl Yazıldı?
* **Amacımız:** Gerçek bir sıcaklık sensörünü simüle etmek ve sürekli veri akışı sağlamaktır.
* **Çalışma Mantığı:** 
  * `Node` sınıfından türetilen `SensorNode` sınıfı başlatılır.
  * Sınıf içerisindeki `create_publisher` fonksiyonu ile `/sicaklik` adında bir `topic` (kanal) tanımlanır. Mesaj tipi olarak standart ROS 2 kütüphanesinden `Float32` seçilmiştir çünkü sıcaklık ondalıklı bir değerdir.
  * `create_timer` fonksiyonu kullanılarak sistemin her 1 saniyede bir tetiklenmesi sağlanır. Her saniye `random.uniform(20.0, 40.0)` komutu ile 20 ile 40 derece arasında gerçekçi rastgele sıcaklık değerleri üretilir ve `/sicaklik` kanalına `publish` edilir.

### 2. `izleyici.py` (Kontrol ve Uyarı Düğümü) Neden ve Nasıl Yazıldı?
* **Amacımız:** Yayınlanan sıcaklık verilerini dinlemek, ekrana raporlamak ve kritik eşik aşım durumlarında sistemi uyarmaktır.
* **Çalışma Mantığı:**
  * `create_subscription` fonksiyonu ile `/sicaklik` kanalına abone olunur. Sensör her veri yayınladığında `listener_callback` fonksiyonu otomatik olarak tetiklenir.
  * Gelen sıcaklık verisi konsola yazdırılır.
  * **Eşik Mantığı:** Belirlenen sınır değerinin (varsayılan: 30°C) üzerine çıkılıp çıkılmadığı `if` bloğu ile kontrol edilir. Eğer değer aşılmışsa, sıradan bir print yerine ROS 2'nin dahili loglama mekanizması olan `get_logger().warn()` fonksiyonu kullanılarak konsolda sarı renkli dikkat çekici bir uyarı logu üretilir.
  * **Bonus (Dinamik Parametre) Mantığı Neden Eklendi?:** Sabit bir eşik değeri yerine, kod üzerinde değişiklik yapmadan bu değeri dışarıdan değiştirebilmek için `declare_parameter('esik_deger', 30.0)` komutu kullanılmıştır. Bu sayede düğüm başlatılırken terminalden eşik değeri esnek bir şekilde değiştirilebilir.

---

## ⚙️ Kurulum ve Çalıştırma Adımları

Projeyi kendi bilgisayarınızda (ROS 2 ortamında) çalıştırmak için sırasıyla şu adımları izleyin:

### Adım 1: Dosyaları Konumlandırma
Paket klasörünü ROS 2 çalışma alanınızın (workspace) `src` dizini altına atın (`~/ros2_ws/src/sicaklik_izleyici_py`).

### Adım 2: Derleme (Build) İşlemi
Bağımlılıkların ve Python betiklerinin sisteme tanıtılması için çalışma alanının kök dizinine gidip `colcon` ile derleme yapın:
```bash
cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
