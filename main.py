import time
from typing import List

# ==========================================
# PERFORMANS ÖLÇÜMÜ (DECORATOR)
# ==========================================
def zaman_olcer(fonksiyon):
    """
    Algoritmaların çalışma süresini milisaniye cinsinden ölçen özel dekoratör.
    Optimizasyon ve zaman karmaşıklığı analizini somutlaştırmak için kullanılmıştır.
    """
    def sarmalayici(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = (bitis - baslangic) * 1000 # Milisaniyeye çevir
        print(f"[{fonksiyon.__name__.upper()}] çalışma süresi: {gecen_sure:.4f} ms")
        return sonuc
    return sarmalayici

# ==========================================
# ALGORİTMA MİMARİSİ (OOP)
# ==========================================
class VeriYapilariAlgoritmalar:
    """
    Arama ve sıralama işlemlerini kapsülleyen sınıf yapısı.
    """

    @staticmethod
    def linear_search(veri_seti: List[int], hedef: int) -> int:
        for indeks, deger in enumerate(veri_seti):
            if deger == hedef:
                return indeks
        return -1

    @staticmethod
    def binary_search(sirali_veri: List[int], hedef: int) -> int:
        sol, sag = 0, len(sirali_veri) - 1
        while sol <= sag:
            # (sol + sag) // 2 yerine taşma (overflow) riskini önleyen güvenli hesaplama
            orta = sol + (sag - sol) // 2 
            
            if sirali_veri[orta] == hedef:
                return orta
            elif sirali_veri[orta] < hedef:
                sol = orta + 1
            else:
                sag = orta - 1
        return -1

    @staticmethod
    @zaman_olcer
    def bubble_sort(veri_seti: List[int]) -> List[int]:
        dizi = veri_seti.copy()
        n = len(dizi)
        for i in range(n):
            degisim_oldu_mu = False
            for j in range(0, n - i - 1):
                if dizi[j] > dizi[j + 1]:
                    dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j]
                    degisim_oldu_mu = True
            # Optimizasyon: Eğer hiç yer değişikliği olmadıysa dizi zaten sıralıdır, döngüyü kır.
            if not degisim_oldu_mu:
                break
        return dizi

    @staticmethod
    @zaman_olcer
    def selection_sort(veri_seti: List[int]) -> List[int]:
        dizi = veri_seti.copy()
        n = len(dizi)
        for i in range(n):
            min_indeks = i
            for j in range(i + 1, n):
                if dizi[j] < dizi[min_indeks]:
                    min_indeks = j
            dizi[i], dizi[min_indeks] = dizi[min_indeks], dizi[i]
        return dizi

    @staticmethod
    @zaman_olcer
    def insertion_sort(veri_seti: List[int]) -> List[int]:
        dizi = veri_seti.copy()
        for i in range(1, len(dizi)):
            anahtar = dizi[i]
            j = i - 1
            while j >= 0 and anahtar < dizi[j]:
                dizi[j + 1] = dizi[j]
                j -= 1
            dizi[j + 1] = anahtar
        return dizi

    @staticmethod
    @zaman_olcer
    def merge_sort(veri_seti: List[int]) -> List[int]:
        # Merge Sort recursive (özyinelemeli) olduğu için zaman ölçümü ana fonksiyonda yapılır
        def _ayir_ve_birlestir(dizi: List[int]) -> List[int]:
            if len(dizi) <= 1:
                return dizi
            
            orta = len(dizi) // 2
            sol_yari = _ayir_ve_birlestir(dizi[:orta])
            sag_yari = _ayir_ve_birlestir(dizi[orta:])
            
            birlestirilmis = []
            i = j = 0
            
            while i < len(sol_yari) and j < len(sag_yari):
                if sol_yari[i] < sag_yari[j]:
                    birlestirilmis.append(sol_yari[i])
                    i += 1
                else:
                    birlestirilmis.append(sag_yari[j])
                    j += 1
                    
            birlestirilmis.extend(sol_yari[i:])
            birlestirilmis.extend(sag_yari[j:])
            return birlestirilmis
            
        return _ayir_ve_birlestir(veri_seti.copy())

# ==========================================
# ÇALIŞTIRMA VE TEST ALANI
# ==========================================
if __name__ == "__main__":
    # Test Verisi
    orijinal_veri = [88, 14, 53, 27, 91, 32, 6, 19, 74, 45]
    print(f"--- Orijinal Veri Seti: {orijinal_veri} ---\n")
    
    # Sınıfı Başlat
    algoritma = VeriYapilariAlgoritmalar()
    
    # --- SIRALAMA TESTLERİ ---
    print(">>> SIRALAMA ALGORİTMALARI PERFORMANS TESTİ <<<")
    bubble_sirali = algoritma.bubble_sort(orijinal_veri)
    selection_sirali = algoritma.selection_sort(orijinal_veri)
    insertion_sirali = algoritma.insertion_sort(orijinal_veri)
    merge_sirali = algoritma.merge_sort(orijinal_veri)
    
    print(f"\nSıralanmış Çıktı Örneği: {merge_sirali}\n")
    
    # --- ARAMA TESTLERİ ---
    aranan_sayi = 53
    print(">>> ARAMA ALGORİTMALARI TESTİ <<<")
    
    linear_indeks = algoritma.linear_search(orijinal_veri, aranan_sayi)
    print(f"Linear Search -> '{aranan_sayi}' sayısı orijinal dizide {linear_indeks}. indekste bulundu.")
    
    binary_indeks = algoritma.binary_search(merge_sirali, aranan_sayi)
    print(f"Binary Search -> '{aranan_sayi}' sayısı sıralı dizide {binary_indeks}. indekste bulundu.")
