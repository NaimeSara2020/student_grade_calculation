# Öğrenci ve Not Takip Uygulaması

Bu proje, Flask kullanarak bir öğrenci ve not takip uygulamasıdır.

## Başlangıç

Bu talimatlar, geliştirme ve test amacıyla yerel makinenizde projenin bir kopyasını nasıl kuracağınızı ve çalıştıracağınızı anlatır. Canlı bir sistem için yapılandırma adımları farklı olabilir.

### Önkoşullar

Projenin çalıştırılması için Python ve pip yüklü olmalıdır.

### Kurulum

1. Depoyu yerel makinenize klonlayın.

    ```bash
    git clone https://github.com/NaimeSara2020/zyfera_test_case.git
    ```

2. Proje dizinine gidin.

    ```bash
    cd proje_adi
    ```

3. Sanal bir ortam oluşturun ve etkinleştirin.

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows için
    source venv/bin/activate  # macOS/Linux için
    ```

4. Gerekli Python kütüphanelerini yükleyin.

    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

5. Veritabanını oluşturun.
    - Terminal veya komut istemcisinde;
    ```bash
    sqlite3
   .open db_name
    ```

6. Uygulamayı çalıştırın.

    ```bash
    python app.py
    ```

## Kullanım

Uygulama çalıştıktan sonra, API rotalarına HTTP istekleri göndererek öğrenci ve not bilgilerini yönetebilirsiniz.
Postman den yararlanabilirsiniz.

### Örnek HTTP İstekleri

1. Öğrenci ekleme:

    ```http
    POST /students
    Content-Type: application/json

    {
        "name": "Öğrenci Adı",
        "surname": "Öğrenci Soyadı",
        "stdNumber": 12345
    }
    ```

2. Not ekleme:

    ```http
    POST /grades
    Content-Type: application/json

    {
        "course_code": "MT101",
        "value": 87,
        "student_id": 12345
    }
    ```

3. Ortalama notu alma:

    ```http
    GET /average_grade/<student_no>
    ```