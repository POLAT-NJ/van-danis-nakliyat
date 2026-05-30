from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Van Danış Evden Eve Nakliyat</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: linear-gradient(to bottom, #eef2ff, #f8fafc);
            color: #222;
        }

        header {
            background: linear-gradient(135deg, #0b1020, #1d4ed8, #7c3aed);
            color: white;
            padding: 90px 20px;
            text-align: center;
        }

        header h1 {
            font-size: 54px;
            margin-bottom: 20px;
        }

        header p {
            font-size: 20px;
            max-width: 750px;
            margin: auto;
            line-height: 1.6;
        }

        .btn {
            display: inline-block;
            margin-top: 30px;
            background: rgba(255,255,255,0.95);
            color: #0f172a;
            padding: 15px 30px;
            border-radius: 12px;
            text-decoration: none;
            font-weight: bold;
        }

        .container {
            width: 90%;
            max-width: 1200px;
            margin: auto;
        }

        section {
            padding: 80px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 50px;
        }

        .section-title h2 {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 25px;
        }

        .card {
            background: rgba(255,255,255,0.95);
            padding: 30px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(37,99,235,0.15);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-10px) scale(1.02);
            border: 1px solid #60a5fa;
        }

        .card h3 {
            margin-bottom: 15px;
            font-size: 24px;
        }

        .about {
            background: rgba(255,255,255,0.95);
        }

        .about-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 40px;
            align-items: center;
        }

        .about-image {
            height: 350px;
            background: #d1d5db;
            border-radius: 20px;
        }

        .stats {
            background: linear-gradient(135deg, #111827, #2563eb);
            color: white;
        }

        .stat-box {
            text-align: center;
        }

        .stat-box h3 {
            font-size: 42px;
            margin-bottom: 10px;
        }

        .contact {
            background: linear-gradient(135deg, #1e3a8a, #6d28d9);
            color: white;
            text-align: center;
        }

        form {
            max-width: 650px;
            margin: 40px auto 0;
        }

        input,
        textarea {
            width: 100%;
            padding: 16px;
            margin-bottom: 18px;
            border: none;
            border-radius: 12px;
            font-size: 16px;
        }

        button {
            padding: 16px 35px;
            border: none;
            border-radius: 12px;
            background: rgba(255,255,255,0.95);
            color: #0f172a;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
        }

        footer {
            background: linear-gradient(135deg, #020617, #111827);
            color: #aaa;
            text-align: center;
            padding: 30px;
        }

        .whatsapp {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: #25D366;
            color: white;
            padding: 15px 20px;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
    </style>
</head>
<body>

<header>
    <div class="container">
        <h1>Van Danış Evden Eve Nakliyat</h1>
        <p>
            Güvenli, hızlı ve profesyonel taşımacılık hizmetleri ile şehir içi ve şehirler arası nakliyatta yanınızdayız.
        </p>
        <a href="#contact" class="btn">Ücretsiz Teklif Al</a>
    </div>
</header>

<section>
    <div class="container">
        <div class="section-title">
            <h2>Hizmetlerimiz</h2>
            <p>Profesyonel taşımacılık çözümleri</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Evden Eve Nakliyat</h3>
                <p>Eşyalarınızı güvenli ve hızlı şekilde yeni adresinize taşıyoruz.</p>
            </div>

            <div class="card">
                <h3>Asansörlü Taşıma</h3>
                <p>Yüksek katlarda güvenli ve pratik taşıma hizmeti sunuyoruz.</p>
            </div>

            <div class="card">
                <h3>Ofis Taşıma</h3>
                <p>Kurumsal taşımacılıkta profesyonel ekip desteği sağlıyoruz.</p>
            </div>

            <div class="card">
                <h3>Eşya Depolama</h3>
                <p>Modern depolama alanlarımızda eşyalarınızı güvenle saklıyoruz.</p>
            </div>
        </div>
    </div>
</section>

<section class="about">
    <div class="container about-content">
        <div class="about-image"></div>

        <div>
            <h2 style="font-size:40px; margin-bottom:20px;">Neden Biz?</h2>
            <p style="line-height:1.8; margin-bottom:20px;">
                Van Danış Evden Eve Nakliyat olarak yıllardır müşteri memnuniyetini ön planda tutuyoruz.
            </p>

            <p style="line-height:1.8; margin-bottom:20px;">
                Uzman kadromuz, modern araçlarımız ve sigortalı taşımacılık hizmetimiz ile güvenli nakliyat sağlıyoruz.
            </p>

            <p style="line-height:1.8;">
                Şehir içi ve şehirler arası taşımacılıkta profesyonel çözümler sunuyoruz.
            </p>
        </div>
    </div>
</section>

<section>
    <div class="container">
        <div class="section-title">
            <h2>Müşteri Yorumları</h2>
            <p>Bizi tercih eden müşterilerimizin görüşleri</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>⭐ ⭐ ⭐ ⭐ ⭐</h3>
                <p style="line-height:1.8; margin-top:15px;">
                    Eşyalarımız sorunsuz taşındı. Profesyonel ekip ve zamanında hizmet.
                </p>
                <strong style="display:block; margin-top:20px;">Ahmet Y.</strong>
            </div>

            <div class="card">
                <h3>⭐ ⭐ ⭐ ⭐ ⭐</h3>
                <p style="line-height:1.8; margin-top:15px;">
                    Paketleme ve taşıma gerçekten çok iyiydi. Kesinlikle tavsiye ederim.
                </p>
                <strong style="display:block; margin-top:20px;">Mehmet K.</strong>
            </div>

            <div class="card">
                <h3>⭐ ⭐ ⭐ ⭐ ⭐</h3>
                <p style="line-height:1.8; margin-top:15px;">
                    Van’dan İstanbul’a sorunsuz taşındık. Çok memnun kaldık.
                </p>
                <strong style="display:block; margin-top:20px;">Zeynep A.</strong>
            </div>
        </div>
    </div>
</section>

<section class="stats">
    <div class="container">
        <div class="grid">
            <div class="stat-box">
                <h3>10+</h3>
                <p>Yıllık Deneyim</p>
            </div>

            <div class="stat-box">
                <h3>5000+</h3>
                <p>Mutlu Müşteri</p>
            </div>

            <div class="stat-box">
                <h3>81</h3>
                <p>Şehre Hizmet</p>
            </div>

            <div class="stat-box">
                <h3>7/24</h3>
                <p>Destek</p>
            </div>
        </div>
    </div>
</section>

<section class="contact" id="contact">
    <div class="container">
        <div class="section-title">
            <h2>İletişim</h2>
            <p>Hemen bizimle iletişime geçin</p>
        </div>

        <form method="POST">
            <input type="text" name="name" placeholder="Ad Soyad" required>
            <input type="tel" name="phone" placeholder="Telefon" required>
            <textarea rows="5" name="message" placeholder="Mesajınız"></textarea>
            <button type="submit">Mesaj Gönder</button>
        </form>
    </div>
</section>

<section>
    <div class="container">
        <div class="section-title">
            <h2>Taşınma Sürecimiz</h2>
            <p>4 adımda güvenli taşınma</p>
        </div>

        <div class="grid">
            <div class="card">
                <h3>1. Ücretsiz Ekspertiz</h3>
                <p>Uzman ekibimiz taşınma planınızı oluşturur.</p>
            </div>

            <div class="card">
                <h3>2. Paketleme</h3>
                <p>Eşyalarınız özel korumalı malzemelerle paketlenir.</p>
            </div>

            <div class="card">
                <h3>3. Güvenli Nakliyat</h3>
                <p>Modern araçlarımız ile güvenli taşıma sağlanır.</p>
            </div>

            <div class="card">
                <h3>4. Yerleştirme</h3>
                <p>Eşyalarınız yeni adresinizde düzenli şekilde teslim edilir.</p>
            </div>
        </div>
    </div>
</section>

<section style="padding:100px 0; background:linear-gradient(135deg,#2563eb,#7c3aed); color:white; text-align:center;">
    <div class="container">
        <h2 style="font-size:48px; margin-bottom:20px;">
            Güvenli Taşımacılık İçin Hemen Arayın
        </h2>

        <p style="font-size:20px; max-width:700px; margin:auto; line-height:1.8;">
            Van Danış Evden Eve Nakliyat ile şehir içi ve şehirler arası profesyonel taşımacılık hizmeti alın.
        </p>

        <a href="#contact" class="btn" style="margin-top:35px;">
            Hemen Teklif Al
        </a>
    </div>
</section>

<footer>
    <h3 style="margin-bottom:10px; color:white;">Van Danış Evden Eve Nakliyat</h3>
    <p>📍 Van / Türkiye</p>
    <p>📞 +90 539 280 75 02</p>
    <p style="margin-top:15px;">© 2026 Tüm Hakları Saklıdır.</p>
</footer>

<a class="whatsapp" href="https://wa.me/905392807502" target="_blank">
    WhatsApp
</a>

</body>
</html>
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        message = request.form.get('message')

        print(f'Yeni Mesaj: {name} | {phone} | {message}')

    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    app.run(debug=True)
