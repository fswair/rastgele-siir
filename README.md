## Antoloji API

Bu API, kullanıcıların Antoloji.com sitesindeki şairleri ve şiirleri aramasını ve rastgele şiirler almasını sağlar. FastAPI kullanılarak oluşturulmuştur.

### İçindekiler
- [Başlarken](#başlarken)
- [Kurulum](#kurulum)
- [Uç Noktalar](#uç-noktalar)
  - [GET /ara/sair](#get-arasair)
  - [GET /ara/siir](#get-arasiir)
  - [GET /rastgele](#get-rastgele)
  - [GET /{endpoint}](#get-endpoint)
  - [GET /siir/{endpoint}](#get-siirendpoint)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

### Başlarken

Bu API'yi kullanmaya başlamak için aşağıdaki talimatları izleyin.

### Kurulum

1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/kullaniciadi/antoloji-api.git
    cd antoloji-api
    ```

2. Gerekli bağımlılıkları yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

3. FastAPI uygulamasını çalıştırın:
    ```bash
    uvicorn main:app --reload
    ```

### Uç Noktalar

#### GET /ara/sair

Bir şairi isme göre arayın.

- **Parametreler:**
  - `sair` (str): Şairin adı.
  - `siirler` (bool | int, opsiyonel): `True` veya `1` olarak ayarlanırsa, yanıt içinde şairin şiirleri de dahil edilir.

- **Yanıt:**
  - `status` (str): İstek durumu.
  - `poet` (str): Şairin Antoloji.com sayfasının URL'si.
  - `poems` (liste, opsiyonel): Şairin şiirlerinin listesi (`siirler` parametresi `True` veya `1` olarak ayarlanmışsa).

Örnek istek:
```bash
GET /ara/sair?sair=Yunus%20Emre&siirler=true
```

Örnek yanıt:
```json
{
  "status": "found",
  "poet": "https://www.antoloji.com/yunus-emre",
  "poems": [
    {
      "title": "Beni Beni",
      "url": "https://www.antoloji.com/beni-beni-siiri/"
    },
    ...
  ]
}
```

#### GET /ara/siir

Şiirleri başlığa veya içeriğe göre arayın.

- **Parametreler:**
  - `siir` (str): Şiirin başlığı veya içeriği.
  - `sayfa` (int, opsiyonel): Sayfa numarası. Varsayılan değer `1`.

- **Yanıt:**
  - Arama sorgusuna uygun şiirlerin listesi.

Örnek istek:
```bash
GET /ara/siir?siir=Aşk&sayfa=2
```

Örnek yanıt:
```json
[
  {
    "title": "Aşk İki Kişiliktir",
    "url": "https://www.antoloji.com/ask-iki-kisiliktir-siiri/",
    "poet": "Ataol Behramoğlu"
  },
  ...
]
```

#### GET /rastgele

Rastgele bir şiir alın.

- **Yanıt:**
  - `endpoint` (str): Şiirin API uç noktası.
  - `title` (str): Şiirin başlığı.
  - `poem` (str): Şiirin içeriği.
  - `url` (str): Şiirin Antoloji.com üzerindeki URL'si.
  - `poet` (dict): Şair hakkında bilgi.
    - `name` (str): Şairin adı.
    - `url` (str): Şairin Antoloji.com sayfasının URL'si.

Örnek istek:
```bash
GET /rastgele
```

Örnek yanıt:
```json
{
  "endpoint": "/siir/ask-iki-kisiliktir-siiri",
  "title": "Aşk İki Kişiliktir",
  "poem": "Aşk bir kişilik değildir...",
  "url": "https://www.antoloji.com/ask-iki-kisiliktir-siiri/",
  "poet": {
    "name": "Ataol Behramoğlu",
    "url": "https://www.antoloji.com/ataol-behramoglu/"
  }
}
```

#### GET /{endpoint}

Belirli bir şiiri uç noktasına göre alın.

- **Parametreler:**
  - `endpoint` (str): Şiirin uç noktası.

- **Yanıt:**
  - `status` (int): İstek durumu (404 eğer bulunamazsa).
  - `message` (str, opsiyonel): Hata mesajı (eğer bulunamazsa).
  - `title` (str, opsiyonel): Şiirin başlığı.
  - `poem` (str, opsiyonel): Şiirin içeriği.
  - `url` (str, opsiyonel): Şiirin Antoloji.com üzerindeki URL'si.
  - `poet` (dict, opsiyonel): Şair hakkında bilgi.
    - `name` (str): Şairin adı.
    - `url` (str): Şairin Antoloji.com sayfasının URL'si.

Örnek istek:
```bash
GET /siir/ask-iki-kisiliktir-siiri
```

Örnek yanıt:
```json
{
  "title": "Aşk İki Kişiliktir",
  "poem": "Aşk bir kişilik değildir...",
  "url": "https://www.antoloji.com/ask-iki-kisiliktir-siiri/",
  "poet": {
    "name": "Ataol Behramoğlu",
    "url": "https://www.antoloji.com/ataol-behramoglu/"
  }
}
```

### Kullanım

API'yi kullanmak için, yukarıda tanımlanan uç noktalara HTTP istekleri gönderebilirsiniz. İşte uç noktaları kullanmanın birkaç örneği:

1. **Bir şair arayın:**
   ```bash
   curl -X GET "http://apiv2.mert.uno/ara/sair?sair=Yunus%20Emre"
   ```

2. **Şiir arayın:**
   ```bash
   curl -X GET "http://apiv2.mert.uno/ara/siir?siir=Aşk&sayfa=1"
   ```

3. **Rastgele bir şiir alın:**
   ```bash
   curl -X GET "http://apiv2.mert.uno/rastgele"
   ```

4. **Belirli bir şiiri uç noktaya göre alın:**
   ```bash
   curl -X GET "http://apiv2.mert.uno/siir/ask-iki-kisiliktir-siiri"
   ```

### Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen depoyu fork edin ve bir pull request oluşturun. Ayrıca, herhangi bir hata veya özellik isteği için issues açabilirsiniz.

### Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
