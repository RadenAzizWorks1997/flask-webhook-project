from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Mendapatkan parameter 'code' dari URL
    code = request.args.get('code')

    if code:
        # Tukar code dengan token akses menggunakan API Instagram (atau Facebook)
        access_token_url = f"https://graph.instagram.com/access_token?client_id={YOUR_APP_ID}&client_secret={YOUR_APP_SECRET}&grant_type=authorization_code&redirect_uri={YOUR_REDIRECT_URI}&code={code}"

        # Mengirimkan permintaan untuk mendapatkan access token
        response = requests.get(access_token_url)
        data = response.json()

        if "access_token" in data:
            # Menyimpan access_token atau proses lebih lanjut
            access_token = data["access_token"]
            return jsonify({"message": "Akses berhasil!", "access_token": access_token})
        else:
            return jsonify({"message": "Gagal mendapatkan access token!"}), 400
    else:
        return jsonify({"message": "Code tidak ditemukan!"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
