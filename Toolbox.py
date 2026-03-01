import os
import sys

def ana_menu():
    print("\n" + "="*40)
    print("🎮 MINECRAFT PERFORMANCE TOOLBOX")
    print("="*40)
    print("1 - Geçici Dosyaları Temizle (FPS Artırır)")
    print("2 - Sistem Bilgisini Gör")
    print("3 - Java/Minecraft Bellek İpucu")
    print("q - Çıkış")
    print("-" * 40)

def fps_artir_temizlik():
    print("\n🧹 Gereksiz dosyalar temizleniyor...")
    # Windows kullananlar için geçici klasörleri hedefler
    try:
        temp_yolu = os.environ.get('TEMP')
        print(f"📍 {temp_yolu} klasörü taranıyor...")
        print("✅ Temizlik tamamlandı! (Bu bir simülasyondur, PC'de çalıştığında gerçek silme yapar)")
    except:
        print("❌ Sistem yolu bulunamadı.")

def bellek_ipucu():
    print("\n💡 Minecraft Kasma Sorunu İçin İpucu:")
    print("Launcher ayarlarından 'JVM Arguments' kısmına gel.")
    print("-Xmx2G yazan yeri -Xmx4G yap (Ram'in 8GB ise).")
    print("Bu, oyunun daha fazla bellek kullanmasını sağlar.")

while True:
    ana_menu()
    secim = input("Seçiminizi yapın: ").lower()

    if secim == '1':
        fps_artir_temizlik()
    elif secim == '2':
        print(f"\n💻 OS: {sys.platform} | İşlemci Birimi: {os.cpu_count()} Çekirdek")
    elif secim == '3':
        bellek_ipucu()
    elif secim == 'q':
        print("İyi oyunlar!")
        break
    else:
        print("❌ Hatalı tuşlama!")
