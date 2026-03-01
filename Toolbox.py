import os
import sys

def ana_menu():
    print("-" * 30)
    print("🚀 BENİM DİJİTAL TOOLBOX'IM")
    print("-" * 30)
    print("1 - Dosya Uzantılarını Listele")
    print("2 - Sistem Bilgilerini Göster")
    print("3 - Klasör Temizliği Yap (Geçici Dosyalar)")
    print("q - Çıkış")
    print("-" * 30)

def dosya_listele():
    print(f"\n📂 Mevcut klasördeki dosyalar: {os.listdir('.')}")

def sistem_bilgisi():
    print(f"\n💻 İşletim Sistemi: {sys.platform}")
    print(f"🐍 Python Versiyonu: {sys.version.split()[0]}")

while True:
    ana_menu()
    secim = input("Bir araç seçin: ").lower()

    if secim == '1':
        dosya_listele()
    elif secim == '2':
        sistem_bilgisi()
    elif secim == '3':
        print("\n🧹 Temizlik simüle ediliyor... (Geliştirilecek)")
    elif secim == 'q':
        print("Görüşürüz!")
        break
    else:
        print("❌ Geçersiz seçim!")

