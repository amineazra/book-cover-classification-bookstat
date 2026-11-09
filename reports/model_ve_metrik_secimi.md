
# Kullanılacak Yöntemler ve Model Mimarileri

## 1. Yöntem Seçiminin Amacı

Bu projede kitap kapağı görüntülerinden 30 farklı kitap kategorisinin tahmin edilmesi amaçlanmaktadır.

Temel problem, çok sınıflı görüntü sınıflandırmasıdır.

BookCover30 veri seti üzerinde dört farklı derin öğrenme mimarisinin karşılaştırılması planlanmaktadır:

1. Basic CNN
2. ResNet50
3. EfficientNet-B0
4. MobileNetV3-Large

Bu modeller; sınıflandırma başarısı, model karmaşıklığı, hesaplama maliyeti ve gerçek bir uygulamada kullanılabilirlik açısından değerlendirilecektir.

## 2. Seçilen Model Mimarileri

### 2.1. Basic CNN

Basic CNN, evrişim katmanları, aktivasyon fonksiyonları, havuzlama katmanları ve sınıflandırma katmanlarından oluşan temel bir derin öğrenme mimarisidir.

Projede karşılaştırma için başlangıç modeli (baseline) olarak kullanılacaktır.

Modelin sıfırdan eğitilmesi planlanmaktadır.

**Avantajları:**
- Basit ve anlaşılabilir mimariye sahiptir.
- Daha az karmaşık bir başlangıç modeli sağlar.
- Diğer mimarilerin katkısını değerlendirmeye yardımcı olur.

**Dezavantajları:**
- Derin mimarilere göre özellik çıkarma kapasitesi sınırlı olabilir.
- Önceden eğitilmiş ağırlıklardan yararlanmadığı için eğitim süreci daha zor olabilir.

### 2.2. ResNet50

ResNet50, 50 katmanlı ve residual bağlantılar kullanan bir CNN mimarisidir.

Residual bağlantılar, bilginin katmanlar arasında daha kolay aktarılmasını sağlayarak derin ağların eğitimindeki bazı zorlukları azaltır.

Projede ImageNet üzerinde önceden eğitilmiş ağırlıklardan yararlanılması planlanmaktadır.

**Avantajları:**
- Güçlü görsel özellik çıkarma kapasitesine sahiptir.
- Transfer learning uygulanabilir.
- Literatürde yaygın olarak kullanılan bir mimaridir.

**Dezavantajları:**
- Temel CNN'e göre daha fazla hesaplama kaynağı gerektirebilir.
- Mobil uygulamalarda kullanımı daha maliyetli olabilir.

### 2.3. EfficientNet-B0

EfficientNet-B0, ağın derinliği, genişliği ve görüntü çözünürlüğü arasındaki ilişkiyi dikkate alan verimli bir CNN mimarisidir.

Projede sınıflandırma başarısı ile hesaplama maliyeti arasındaki dengeyi incelemek için kullanılacaktır.

**Avantajları:**
- Parametreleri verimli kullanmayı hedefler.
- Transfer learning için uygundur.
- Hesaplama maliyeti ve başarı açısından dengeli bir alternatif olabilir.

**Dezavantajları:**
- Basit CNN'e göre daha karmaşık bir yapıya sahiptir.
- Gerçek performansı veri setine ve eğitim koşullarına bağlıdır.

### 2.4. MobileNetV3-Large

MobileNetV3, özellikle kaynakları sınırlı cihazlarda verimli çalışmak amacıyla geliştirilmiş bir CNN mimarisidir.

Depthwise separable convolution ve dikkat mekanizmaları gibi bileşenlerden yararlanır.

Projede BookStat uygulamasına olası entegrasyon açısından hafif bir model alternatifi olarak değerlendirilecektir.

**Avantajları:**
- Verimli çıkarım yapmayı hedefler.
- Mobil ve kaynakları sınırlı ortamlarda kullanım için tasarlanmıştır.
- Model boyutu ve çıkarım hızı açısından avantaj sağlayabilir.

**Dezavantajları:**
- Bazı problemlerde daha büyük modellerden düşük doğruluk elde edebilir.
- Gerçek cihaz performansı ayrıca ölçülmelidir.

## 3. Model Karşılaştırma Planı

Modellerin mümkün olduğunca karşılaştırılabilir koşullarda değerlendirilmesi planlanmaktadır.

- Ana veri seti: BookCover30
- Toplam görüntü sayısı: 57.000
- Sınıf sayısı: 30
- Eğitim: 41.040 görüntü
- Doğrulama: 10.260 görüntü
- Test: 5.700 görüntü
- Giriş boyutu: 224×224 piksel
- Görüntü formatı: RGB
- Başlangıç batch size: 32

Temel CNN sıfırdan eğitilecek, diğer üç model için önceden eğitilmiş ağırlıklarla transfer learning uygulanması planlanacaktır.

Model ağırlıklarının gerektirdiği ön işleme dönüşümleri dikkate alınacaktır.

Eğitim parametreleri, model boyutu ve donanım kullanımına göre sonraki fazda kesinleştirilecektir.

Orijinal test kümesi, model seçimi ve hiperparametre ayarlaması için kullanılmayacaktır.

## 4. Değerlendirme Metrikleri

### 4.1. Accuracy

Doğru tahmin edilen örneklerin toplam örnek sayısına oranıdır.

Modelin genel sınıflandırma başarısını değerlendirmek için kullanılacaktır.

### 4.2. Precision

Bir kategori için pozitif olarak tahmin edilen örneklerin ne kadarının gerçekten o kategoriye ait olduğunu ölçer.

Yanlış pozitif tahminleri incelememizi sağlar.

### 4.3. Recall

Bir kategoriye ait gerçek örneklerin ne kadarının model tarafından doğru bulunduğunu ölçer.

Yanlış negatif tahminleri incelememizi sağlar.

### 4.4. Macro-F1 Score

Her kategori için hesaplanan F1 değerlerinin aritmetik ortalamasıdır.

Sınıfların performansını eşit ağırlıkla değerlendirdiği için kullanılacaktır.

### 4.5. Top-1 Accuracy

Modelin en yüksek olasılık verdiği kategorinin gerçek kategoriyle eşleşme oranıdır.

### 4.6. Top-5 Accuracy

Gerçek kategorinin, modelin en yüksek olasılık verdiği ilk beş kategori arasında bulunma oranıdır.

### 4.7. Confusion Matrix

Gerçek kategoriler ile tahmin edilen kategoriler arasındaki ilişkiyi gösterir.

Hangi kitap kategorilerinin birbirleriyle karıştırıldığını incelemek için kullanılacaktır.

## 5. Genel Değerlendirme

Dört farklı mimarinin karşılaştırılmasıyla yalnızca en yüksek doğruluğu elde eden model değil, hesaplama maliyeti ve uygulama açısından daha dengeli modeller de belirlenmeye çalışılacaktır.

Özellikle MobileNetV3-Large modelinin, BookStat uygulamasına gelecekteki entegrasyon potansiyeli açısından değerlendirilmesi planlanmaktadır.

Goodreads Best Books Ever veri setinden oluşturulan ve etiketleri yeterince doğrulanan bir alt küme ise farklı veri kaynağında ek değerlendirme amacıyla kullanılabilecektir.

Goodreads üzerindeki değerlendirme, veri setleri arasındaki kategori farklılıkları dikkate alınarak ana BookCover30 test sonuçlarından ayrı raporlanacaktır.

Bu aşamada mimariler ve değerlendirme stratejisi planlanmıştır. Model eğitimleri ve gerçek performans sonuçları Faz 2 kapsamında gerçekleştirilecektir.