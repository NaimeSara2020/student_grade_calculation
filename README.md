# Öğrenci ve Not Takip Uygulaması

Bu proje, Flask kullanarak bir öğrenci ve not takip uygulamasıdır.

## Başlangıç

Bu talimatlar, geliştirme ve test amacıyla yerel makinenizde projenin bir kopyasını nasıl kuracağınızı ve çalıştıracağınızı anlatır. Canlı bir sistem için yapılandırma adımları farklı olabilir.

### Önkoşullar

Projenin çalıştırılması için Python ve pip yüklü olmalıdır.

### Kurulum

1. Depoyu yerel makinenize klonlayın.

    ```bash
    git clone https://github.com/NaimeSara2020/student_grade_calculation.git
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
   

# Student and Grade Tracking Application

This project is a student and grade tracking application using Flask.

## Getting Started

These instructions will guide you through setting up and running a copy of the project on your local machine for development and testing purposes. Configuration steps may differ for a live system.

### Prerequisites

Python and pip must be installed to run the project.

### Installation

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/NaimeSara2020/student_grade_calculation.git
    ```

2. Navigate to the project directory.

    ```bash
    cd project_name
    ```

3. Create and activate a virtual environment.

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # For Windows
    source venv/bin/activate  # For macOS/Linux
    ```

4. Install the required Python libraries.

    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

5. Create the database.
    - In the terminal or command prompt;
    ```bash
    sqlite3
   .open db_name
    ```

6. Run the application.

    ```bash
    python app.py
    ```

## Usage

After the application is running, you can manage student and grade information by sending HTTP requests to the API routes. You can use Postman for this purpose.

### Sample HTTP Requests

1. Adding a student:

    ```http
    POST /students
    Content-Type: application/json

    {
        "name": "Student Name",
        "surname": "Student Surname",
        "stdNumber": 12345
    }
    ```

2. Adding a grade:

    ```http
    POST /grades
    Content-Type: application/json

    {
        "course_code": "MT101",
        "value": 87,
        "student_id": 12345
    }
    ```

3. Getting the average grade:

    ```http
    GET /average_grade/<student_no>
    ```
