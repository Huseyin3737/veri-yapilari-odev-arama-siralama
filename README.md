# Veri Yapıları Arama ve Sıralama Ödevi - Hüseyin Altun

Bu projede derste işlediğimiz temel arama ve sıralama algoritmalarını Python diliyle hazırladım. Kodları yazarken sadece çalışmasına değil, aynı zamanda düzenli olmasına ve ne kadar hızlı çalıştığını görebilmeye odaklandım.

## Kodun Yapısı Hakkında

Ödevdeki kodları `VeriYapilariAlgoritmalar` isimli bir sınıf (class) içinde topladım. Bu sayede bütün algoritmalar tek bir yerden yönetilebiliyor. Ayrıca kodun içine `@zaman_olcer` adında bir yapı ekledim. Bu yapı sayesinde hangi algoritmayı çalıştırırsak çalıştıralım, terminal ekranında o algoritmanın kaç milisaniyede bittiğini otomatik olarak görebiliyoruz. 

## Uyguladığım Algoritmalar

### 1. Sıralama Yöntemleri
* **Bubble Sort:** Klasik kabarcık sıralama. Kodun içine bir kontrol ekleyerek, eğer dizi zaten sıralıysa boşuna dönmemesini (optimizasyon) sağladım.
* **Selection Sort:** Her adımda en küçük sayıyı bulup başa alan yöntem.
* **Insertion Sort:** Sayıları tek tek alıp olması gereken yere yerleştirerek ilerleyen sistem.
* **Merge Sort:** Diziyi sürekli ikiye bölüp en sonunda birleştirerek sıralayan en hızlı yöntemlerden biri. Recursive (özyinelemeli) bir yapısı var.

### 2. Arama Yöntemleri
* **Linear Search:** Dizideki her elemanı tek tek kontrol eden basit arama.
* **Binary Search:** Sadece sıralı dizilerde çalışan, her adımda arama alanını yarıya indirerek çok hızlı sonuç veren algoritma.

## Performans Tablosu (Big-O)

Algoritmaların teorik hızlarını şu şekilde özetleyebilirim:

| Algoritma | Karmaşıklık (Ortalama) |
| :--- | :--- |
| **Merge Sort** | O(n log n) |
| **Selection Sort** | O(n^2) |
| **Binary Search** | O(log n) |
| **Linear Search** | O(n) |

## Nasıl Çalıştırılır?
Bilgisayarınızda Python yüklüyse, terminale `python ana.py` yazmanız yeterlidir. Program çalıştığında önce orijinal diziyi, sonra her bir algoritmanın çalışma süresini raporlayacaktır.

---
**Hazırlayan:** Hüseyin Altun  
**Bölüm:** Yapay Zeka Operatörlüğü  
**Ders:** Veri Yapıları ve Algoritmalar
