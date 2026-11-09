
# Literatür Taraması: Kitap Kapağından Tür Sınıflandırması

## 1. Literatür Taramasının Amacı

Bu çalışmada kitap kapağı görüntülerinden kitap türü veya kategorisi tahmin edilmesine yönelik derin öğrenme yöntemleri incelenmiştir.

Literatür taramasının temel amacı, önceki araştırmalarda kullanılan veri setlerini, model mimarilerini, değerlendirme metriklerini ve elde edilen sonuçları karşılaştırarak geliştirilecek sınıflandırma sistemi için uygun yöntemleri belirlemektir.

Bu kapsamda BookCover30 veri seti üzerinde gerçekleştirilen çalışmalar ile Goodreads kaynaklı kitap kapaklarını kullanan araştırmalar değerlendirilmiştir.

## 2. İlgili Akademik Çalışmalar

### 2.1. Jolly ve Arkadaşları (2018)

**Makale:** How do Convolutional Neural Networks Learn Design?

**Yazarlar:** Shailza Jolly, Brian Kenji Iwana, Ryohei Kuroki ve Seiichi Uchida.

**Veri seti:** Kitap kapağı görüntülerinden oluşan tür sınıflandırma verisi.

**Yöntem:** Convolutional Neural Networks (CNN) ve Layer-wise Relevance Propagation (LRP).

Bu çalışmada CNN modellerinin kitap kapaklarından tür tahmini yaparken hangi görsel özelliklerden yararlandığı araştırılmıştır.

LRP yöntemi kullanılarak modelin kararını etkileyen görüntü bölgeleri analiz edilmiştir. Ayrıca nesne ve metin algılama yöntemleriyle kapak tasarımlarındaki türlere özgü unsurlar incelenmiştir.

**Temel bulgu:** Kitap kapaklarındaki görsel tasarım unsurları tür sınıflandırması açısından bilgi taşımaktadır. Modelin kararında etkili olan bölgelerin incelenmesi, sınıflandırmanın açıklanabilirliğine katkı sağlamaktadır.

**Projemize katkısı:** Geliştireceğimiz modellerin yalnızca tahmin başarısı değil, hangi kapak özelliklerinden yararlandığı da gelecekte açıklanabilir yapay zekâ yöntemleriyle incelenebilir.

**DOI:** https://doi.org/10.1109/ICPR.2018.8545624

### 2.2. Lucieri ve Arkadaşları (2020)

**Makale:** Benchmarking Deep Learning Models for Classification of Book Covers

**Veri seti:** BookCover30'un incelenmiş ve düzeltilmiş alt kümesi.

**Yöntem:** NASNet, ResNet50, ResNet152, VGG16, DenseNet161 ve diğer derin öğrenme mimarileri.

Çalışmada kitap kapaklarının yalnızca görsel içeriklerinden kategori tahmini yapılmasının ne ölçüde mümkün olduğu araştırılmıştır.

Farklı CNN mimarileri karşılaştırılmış ve modellerin kapak görüntülerindeki ayırt edici özellikleri öğrenme yetenekleri değerlendirilmiştir.

**Temel bulgu:** Veri setinin yayımlanan karşılaştırma sonuçlarında NASNet için yaklaşık %30,5 doğruluk raporlanmıştır. Güçlü görüntü sınıflandırma mimarilerinin bile bu problemde sınırlı başarı göstermesi, kitap kapağından tür tahmininin zor bir görev olduğunu ortaya koymaktadır.

**Projemize katkısı:** Birden fazla mimariyi aynı veri bölünmesi üzerinde karşılaştırmanın önemini göstermektedir. Ayrıca model karmaşıklığının artmasının her zaman daha yüksek sınıflandırma başarısı sağlamayabileceğini düşündürmektedir.

**DOI:** https://doi.org/10.1007/s42979-020-00132-z

### 2.3. Kundu ve Zheng (2020)

**Makale:** Deep Multi-modal Networks for Book Genre Classification Based on Its Cover

**Veri seti:** BookCover30.

**Yöntem:** CNN tabanlı görsel modeller, kapak metninin çıkarılması, metin modelleri ve çok modlu derin öğrenme.

Bu çalışmada yalnızca kitap kapağı görüntüsü kullanmanın yanında kapak üzerindeki metinsel bilgilerin de sınıflandırmaya katkısı araştırılmıştır.

Görüntü tabanlı modellerin yanı sıra OCR ile elde edilen metin özelliklerini kullanan modeller geliştirilmiştir.

Görsel ve metinsel özellikler, basit birleştirme ve Deep Canonical Correlation Analysis (DCCA) gibi yöntemlerle bir araya getirilmiştir.

**Temel sonuçlar:**

- ResNet50, görüntü tabanlı modeller arasında en başarılı seçeneklerden biri olmuştur.
- Basit görsel ve metinsel özellik birleştirme yaklaşımı %56,1 Top-1 ve %77,7 Top-3 doğruluğa ulaşmıştır.
- DCCA tabanlı birleştirme yaklaşımı %48,9 Top-1 ve %72,3 Top-3 doğruluk sağlamıştır.

**Projemize katkısı:** Kitap kapaklarında metinlerin önemli bilgi taşıdığını göstermektedir. Projemizin ilk aşamasında görsel modeller karşılaştırılacak; OCR destekli çok modlu sınıflandırma ise ileride uygulanabilecek bir geliştirme olarak değerlendirilecektir.

**ArXiv DOI:** https://doi.org/10.48550/arXiv.2011.07658

**Not:** Bu kaynak bir arXiv ön baskısıdır.

### 2.4. Buczkowski ve Arkadaşları (2018)

**Makale:** Deep Learning Approaches towards Book Covers Classification

**Yazarlar:** Przemyslaw Buczkowski, Antoni Sobkowicz ve Marek Kozlowski.

**Veri seti:** Goodreads kaynaklı, yaklaşık 160.000 kitap kapağı içeren araştırma verisi.

**Yöntem:** İki farklı CNN mimarisi.

Araştırmacılar Goodreads'ten elde ettikleri kitap kapağı görüntüleri üzerinde otomatik tür sınıflandırması gerçekleştirmiştir.

Çalışmada en yaygın 13 tür ve diğer türleri temsil eden bir "Other" kategorisi kullanılarak toplam 14 sınıflı bir problem oluşturulmuştur.

Basit CNN mimarisi ile daha karmaşık bir CNN mimarisi karşılaştırılmıştır.

**Temel sonuçlar:**

- Daha basit CNN modeli yaklaşık %61 doğruluk elde etmiştir.
- Daha karmaşık CNN modeli yaklaşık %58 doğruluk elde etmiştir.
- Basit model hem performans hem de eğitim süreci açısından daha avantajlı bulunmuştur.

**Projemize katkısı:** Goodreads kaynaklı kapak görüntülerinin sınıflandırma çalışmalarında kullanılabileceğini göstermektedir. Ayrıca daha karmaşık mimarilerin her zaman daha başarılı olmadığını desteklemektedir.

Bu araştırmanın kullandığı Goodreads veri seti ile projemizde kullanılan Best Books Ever Dataset aynı veri seti değildir.

**DOI:** https://doi.org/10.5220/0006556103090316

### 2.5. Zeng ve Arkadaşları (2025)

**Makale:** Novel Dual Convolution Adaptive Focus Neural Network for Book Genre Classification

**Veri seti:** 30 kategorili kitap kapağı sınıflandırma verisi.

**Yöntem:** YOLOv8 tabanlı geliştirilmiş CPPDE-YOLO mimarisi.

Çalışmada kitap kapağı görüntülerinden daha etkili özellikler çıkarabilmek amacıyla YOLOv8 mimarisi üzerinde değişiklikler gerçekleştirilmiştir.

PConv, PWConv, dikkat mekanizmaları ve dinamik örnekleme gibi bileşenler kullanılarak sınıflandırma performansının iyileştirilmesi hedeflenmiştir.

**Temel sonuçlar:**

| Model | Top-1 Accuracy | Top-5 Accuracy |
|---|---:|---:|
| YOLOv8 | %29,6 | %61,7 |
| CPPDE-YOLO | %30,7 | %62,7 |

Önerilen mimari, YOLOv8 modeline göre Top-1 doğruluğunda 1,1 yüzde puan, Top-5 doğruluğunda 1,0 yüzde puan iyileşme sağlamıştır.

**Projemize katkısı:** Kitap kapağı sınıflandırmasında dikkat mekanizmaları ve gelişmiş özellik çıkarma yöntemlerinin potansiyelini göstermektedir.

**DOI:** https://doi.org/10.1371/journal.pone.0331011

## 3. Akademik Çalışmaların Karşılaştırılması

| Çalışma | Yıl | Veri Seti | Yöntem | Öne Çıkan Sonuç |
|---|---|---|---|---|
| Jolly ve ark. | 2018 | Kitap kapakları | CNN + LRP | Görsel özelliklerin açıklanması |
| Lucieri ve ark. | 2020 | BookCover30 alt kümesi | Çoklu CNN karşılaştırması | NASNet yaklaşık %30,5 |
| Kundu ve Zheng | 2020 | BookCover30 | Görsel + OCR + multimodal | %56,1 Top-1 |
| Buczkowski ve ark. | 2018 | Goodreads kaynaklı | İki CNN mimarisi | Basit CNN yaklaşık %61 |
| Zeng ve ark. | 2025 | 30 kategorili kapak verisi | CPPDE-YOLO | %30,7 Top-1 |

**Karşılaştırma notu:** Bu çalışmalar farklı veri bölünmeleri, sınıf sayıları ve değerlendirme protokolleri kullanabilmektedir. Bu nedenle raporlanan doğruluk değerleri doğrudan aynı koşullarda elde edilmiş sonuçlar olarak değerlendirilmemelidir.

## 4. Kullanılan Yöntemlerin Analizi

### 4.1. CNN Tabanlı Yaklaşımlar

CNN mimarileri, görüntülerdeki renk, kenar, doku ve şekil gibi özellikleri otomatik olarak öğrenebilmektedir.

Kitap kapağı sınıflandırmasında CNN yöntemleri temel bir başlangıç noktası oluşturmaktadır.

**Avantajları:**
- Görsel özellikleri otomatik öğrenir.
- Farklı derinlik ve karmaşıklıklarda geliştirilebilir.
- Temel CNN mimarileri karşılaştırma modeli olarak kullanılabilir.

**Dezavantajları:**
- Görsel açıdan benzer kategorileri ayırt etmekte zorlanabilir.
- Kitap kapağındaki yazıları doğrudan anlamlandırma yeteneği sınırlıdır.
- Daha karmaşık modellerin hesaplama maliyeti artabilir.

### 4.2. Önceden Eğitilmiş Derin Öğrenme Mimarileri

ResNet gibi modeller, ImageNet üzerinde öğrenilen görsel özelliklerden yararlanarak transfer learning uygulanmasına imkân tanımaktadır.

Bu yaklaşım, sıfırdan model eğitmeye alternatif olarak değerlendirilebilir.

**Avantajları:**
- Önceden öğrenilmiş görsel özelliklerden yararlanabilir.
- Derin mimarilerin eğitimini kolaylaştırabilir.
- Farklı mimarilerin aynı veri üzerinde karşılaştırılmasını sağlar.

**Dezavantajları:**
- Model boyutu ve hesaplama maliyeti yüksek olabilir.
- Ön eğitim verileri ile kitap kapakları arasındaki alan farklılığı performansı etkileyebilir.

### 4.3. Çok Modlu Yaklaşımlar

Çok modlu yöntemler, kitap kapağındaki görseller ile OCR kullanılarak çıkarılan metinleri birlikte değerlendirir.

Kundu ve Zheng'in çalışması, bu yaklaşımın yalnızca görsel kullanan modellere göre daha başarılı olabileceğini göstermektedir.

Bununla birlikte OCR sistemleri ve metinsel özellik çıkarma işlemleri ek hesaplama maliyeti ve yazılım karmaşıklığı oluşturabilir.

## 5. Literatürün Genel Değerlendirilmesi

İncelenen çalışmalar sonucunda kitap kapağından tür sınıflandırmasının, kategoriler arasındaki görsel benzerlikler ve kapak tasarımlarındaki çeşitlilik nedeniyle zor bir problem olduğu görülmüştür.

Çalışmalarda CNN ve transfer learning yöntemleri yaygın olarak kullanılmıştır. Bununla birlikte gelişmiş mimarilerin her zaman belirgin performans artışı sağlamadığı anlaşılmaktadır.

Görsel özelliklere ek olarak kapak üzerindeki metinsel bilgilerin kullanılması sınıflandırma başarısını artırabilmektedir.

Farklı veri kaynakları arasında sınıf tanımları ve etiketleme biçimleri değişebildiğinden, veri setlerinin doğrudan birleştirilmesi veya farklı çalışmaların başarı oranlarının doğrudan karşılaştırılması uygun değildir.

Bu proje kapsamında önce BookCover30 üzerinde farklı görüntü sınıflandırma mimarileri ortak koşullarda değerlendirilecektir.

Ardından Goodreads Best Books Ever veri setinden seçilen ve etiketleri doğrulanan kapaklar üzerinde dış değerlendirme yapılarak farklı veri kaynaklarına genelleme yeteneği incelenecektir.

Projenin temel hedefi yeni bir mimari geliştirmekten ziyade mevcut yaklaşımları sistematik biçimde karşılaştırmak ve elde edilen sonuçları BookStat uygulamasında kullanılabilecek bir sınıflandırma modülüne temel oluşturmaktır.

## 6. Kaynakça

[1] Jolly, S., Iwana, B. K., Kuroki, R., & Uchida, S. (2018). How do Convolutional Neural Networks Learn Design? 24th International Conference on Pattern Recognition (ICPR), 1085–1090. DOI: 10.1109/ICPR.2018.8545624.

[2] Lucieri, A., et al. (2020). Benchmarking Deep Learning Models for Classification of Book Covers. SN Computer Science, 1, Article 139. https://doi.org/10.1007/s42979-020-00132-z

[3] Kundu, C., & Zheng, L. (2020). Deep Multi-modal Networks for Book Genre Classification Based on Its Cover. arXiv preprint. https://doi.org/10.48550/arXiv.2011.07658

[4] Buczkowski, P., Sobkowicz, A., & Kozlowski, M. (2018). Deep Learning Approaches towards Book Covers Classification. Proceedings of ICPRAM, 309–316. https://doi.org/10.5220/0006556103090316

[5] Zeng, Q., et al. (2025). Novel Dual Convolution Adaptive Focus Neural Network for Book Genre Classification. PLOS ONE, 20(11), e0331011. https://doi.org/10.1371/journal.pone.0331011
