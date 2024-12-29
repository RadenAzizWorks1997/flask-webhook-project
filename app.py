from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/callback')
def callback():
    try:
        # Ambil parameter 'code' dari URL
        code = request.args.get('code')

        # Jika 'code' tidak ada
        if not code:
            return jsonify(message="Code tidak ditemukan!"), 400

        # Proses 'code' untuk mendapatkan token akses dari Instagram
        access_token_url = f"https://graph.instagram.com/access_token?client_id={1671248000474432}&client_secret={6d7162c3ca1654ed02bad976e9db516c}&grant_type=authorization_code&redirect_uri={YOUR_REDIRECT_URI}&code={code}"

        # Mengirimkan permintaan untuk mendapatkan access token
        response = requests.get(access_token_url)
        data = response.json()

        # Menyimpan access_token atau proses lebih lanjut
        if "access_token" in data:
            access_token = data["access_token"]
            return jsonify({"message": "Akses berhasil!", "access_token": access_token})
        else:
            return jsonify({"message": "Gagal mendapatkan access token!"}), 400

    except Exception as e:
        # Tangani jika terjadi error lainnya
        return jsonify(message="Terjadi kesalahan pada server", error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
