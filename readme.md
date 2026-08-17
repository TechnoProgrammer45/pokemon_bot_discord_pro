# 🎮 Discord Pokemon Savaş Botu 🐉

Selam! Bu benim Kodland Python kursu için hazırladığım Discord bot projem. Sunucuda arkadaşlarınızla kendi pokemonlarınızı oluşturup birbiriyle kapıştırabiliyorsunuz. Bayağı eğlenceli bir proje oldu bence! 

## 🚀 Neler Yapabiliyor? (Komutlar)

Botun temel komutları şunlar:

* **`!go`** : Kendinize rastgele bir Pokemon oluşturursunuz. %60 normal, %20 Sihirbaz (Wizard), %20 Dövüşçü (Fighter) çıkma ihtimali var. Şansınıza ne gelirse! 🎲
* **`!info`** : Kendi Pokemon'unuzun canını (HP), gücünü ve API'den çektiği resmini gösterir.
* **`!attack @kullanıcı`** : Arkadaşınızın Pokemon'una saldırırsınız. Dövüşçü pokemonlar bazen süper vuruş yapabiliyor, sihirbazlar da şanslıysa kalkan açıp hasarı tamamen sıfırlayabiliyor.
* **`!feed`** : Savaşta canı azalan Pokemon'unuzu besleyip HP'sini dolduruyorsunuz. Ama sürekli art arda besleyemezsiniz, acıkmaları için biraz süre geçmesi lazım (süre kontrolü ekledim ⏳).

## 📸 Ekran Görüntüleri

Botu sunucumda denerken aldığım bir görüntü (Can yenileme testi):

![Bot Test ve Feed Komutu](image_f96d9e.jpg)

*(Buraya ileride arkadaşlarımla savaşırken aldığım aksiyonlu SS'leri de ekleyeceğim)*

## 💻 Kodun Arka Planı (Nasıl Yaptım?)

Projeyi yazarken OOP (Nesne Yönelimli Programlama) mantığını kullandım. Temel bir `Pokemon` ana sınıfı var, `Wizard` ve `Fighter` sınıfları bundan miras alıyor (Inheritance). 

En sevdiğim kısım Polymorphism (Çok biçimlilik) oldu. Mesela `feed()` metodu hepsinde var ama Dövüşçü pokemonda daha fazla can veriyor, Sihirbaz pokemonda ise besleme bekleme süresi çok daha kısa! 

## ⚙️ Kurulum
Eğer kodları incelemek veya kendi sunucunuza kurmak isterseniz dosyaları indirip `config.py` içine kendi bot token'ınızı yazmanız yeterli. 

Buraya kadar okuduğunuz için teşekkürler.
