from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Database 50 Kata (Saya masukkan beberapa contoh utama, kamu bisa teruskan hingga 50)
database_kamus = [
    {"daerah": "aina", "indonesia": "Jangan", "asal": "Bima"},
    {"daerah": "dahu", "indonesia": "Takut", "asal": "Bima"},
    {"daerah": "Mada", "indonesia": "Saya", "asal": "Bima"},
    {"daerah": "Kita", "indonesia": "Kita", "asal": "Bima"},
    {"daerah": "Ngaha", "indonesia": "Makan", "asal": "Bima"},
    {"daerah": "nono", "indonesia": "Minum", "asal": "Bima"},
    {"daerah": "Lampa", "indonesia": "Jalan", "asal": "Bima"},
    {"daerah": "Taho", "indonesia": "Baik", "asal": "Bima"},
    {"daerah": "Oi", "indonesia": "Air", "asal": "Bima"},
    {"daerah": "Uma", "indonesia": "Rumah", "asal": "Bima"},
    {"daerah": "Wade", "indonesia": "Jangan", "asal": "Bima"},
    {"daerah": "Taku", "indonesia": "Takut", "asal": "Bima"},
    {"daerah": "Mada", "indonesia": "Saya", "asal": "Bima"},
    {"daerah": "Kita", "indonesia": "Kita", "asal": "Bima"},
    {"daerah": "Ngami", "indonesia": "Makan", "asal": "Bima"},
    {"daerah": "Moi", "indonesia": "Minum", "asal": "Bima"},
    {"daerah": "Lampa", "indonesia": "Jalan", "asal": "Bima"},
    {"daerah": "Taho", "indonesia": "Baik", "asal": "Bima"},
    {"daerah": "Oi", "indonesia": "Air", "asal": "Bima"},
    {"daerah": "Uma", "indonesia": "Rumah", "asal": "Bima"},
    {"daerah": "Kasama weki", "indonesia": "Selamat datang", "asal": "Bima"},
    {"daerah": "Beru", "indonesia": "Baru", "asal": "Bima"},
    {"daerah": "Nahu", "indonesia": "Aku", "asal": "Bima"},
    {"daerah": "Tidore", "indonesia": "Tidur", "asal": "Bima"},
    {"daerah": "Pahu", "indonesia": "Wajah", "asal": "Bima"},
    {"daerah": "Oru", "indonesia": "Lari", "asal": "Bima"},
    {"daerah": "Mawo", "indonesia": "Teduh", "asal": "Bima"},
    {"daerah": "Afu", "indonesia": "Api", "asal": "Bima"},
    {"daerah": "Wadu", "indonesia": "Batu", "asal": "Bima"},
    {"daerah": "Dana", "indonesia": "Tanah", "asal": "Bima"},
    {"daerah": "Langi", "indonesia": "Langit", "asal": "Bima"},
    {"daerah": "Bura", "indonesia": "Putih", "asal": "Bima"},
    {"daerah": "Me'e", "indonesia": "Hitam", "asal": "Bima"},
    {"daerah": "Kala", "indonesia": "Merah", "asal": "Bima"},
    {"daerah": "Raba", "indonesia": "Hangat", "asal": "Bima"},
    {"daerah": "Midi", "indonesia": "Dingin", "asal": "Bima"},
    {"daerah": "Tua", "indonesia": "Tua", "asal": "Bima"},
    {"daerah": "Kandai", "indonesia": "Tiang", "asal": "Bima"},
    {"daerah": "Ncoki", "indonesia": "Sempit", "asal": "Bima"},
    {"daerah": "Mbalo", "indonesia": "Lebar", "asal": "Bima"},
    {"daerah": "Kone", "indonesia": "Kucing", "asal": "Bima"},
    {"daerah": "Nggahi", "indonesia": "Bicara", "asal": "Bima"},
    {"daerah": "Rawi", "indonesia": "Kerja", "asal": "Bima"},
    {"daerah": "Lingi", "indonesia": "Rindu", "asal": "Bima"},
    {"daerah": "Bade", "indonesia": "Tahu", "asal": "Bima"},
    {"daerah": "Wara", "indonesia": "Ada", "asal": "Bima"},
    {"daerah": "Ma'a", "indonesia": "Malu", "asal": "Bima"},
    {"daerah": "Mori", "indonesia": "Hidup", "asal": "Bima"},
    {"daerah": "Made", "indonesia": "Mati", "asal": "Bima"},
    {"daerah": "Tada", "indonesia": "Kenal", "asal": "Bima"},
    {"daerah": "Nggori", "indonesia": "Goyang", "asal": "Bima"},
    {"daerah": "Mboto", "indonesia": "Banyak", "asal": "Bima"},
    {"daerah": "Sidi", "indonesia": "Sedikit", "asal": "Bima"},
    {"daerah": "Doro", "indonesia": "Gunung", "asal": "Bima"},
    {"daerah": "Bune habata?", "indonesia": "apa kabar?", "asal": "Bima"},
    {"daerah": "Campa", "indonesia": "Pecah", "asal": "Bima"},
    {"daerah": "Tunti", "indonesia": "Tulis", "asal": "Bima"},
    {"daerah": "Baca", "indonesia": "Baca", "asal": "Bima"},
    {"daerah": "Dou", "indonesia": "Orang", "asal": "Bima"},
    {"daerah": "Maju", "indonesia": "Rusa", "asal": "Bima"}
]
    # Lanjutkan daftar ini sampai 50 kata...


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    teks = data.get('query', '').lower().strip()
    if not teks: return jsonify({"hasil": ""})

    # Logika memecah kalimat dan mencocokkan kata
    kata_kata = teks.split()
    hasil = []
    for k in kata_kata:
        match = next((i['daerah'] for i in database_kamus if i['indonesia'].lower() == k), None)
        hasil.append(match if match else f"({k})")
    
    return jsonify({"hasil": " ".join(hasil)})

if __name__ == '__main__':
    app.run(debug=True)