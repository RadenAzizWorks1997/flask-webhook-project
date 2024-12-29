from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Mendapatkan parameter 'code' dari URL
    code = request.args.get('code')

    if code:
        # Tukar code dengan token akses menggunakan API Instagram (atau Facebook)
        access_token_url = f"https://graph.instagram.com/access_token?client_id=1671248000474432&client_secret=6d7162c3ca1654ed02bad976e9db516c&grant_type=authorization_code&redirect_uri=https://web-production-9ffce.up.railway.app/callback&code={code}"
        
        try:
            # Mengirimkan permintaan untuk mendapatkan access token
            response = requests.get(access_token_url)
            print(f"Response Status Code: {response.status_code}")  # Log status code
            print(f"Response Text: {response.text}")  # Log response text untuk debug

            # Cek apakah responsnya valid dan JSON
            if response.status_code == 200:
                data = response.json()
                if "access_token" in data:
                    access_token = data["access_token"]
                    return jsonify({"message": "Akses berhasil!", "access_token": access_token})
                else:
                    return jsonify({"message": "Gagal mendapatkan access token!"}), 400
            else:
                return jsonify({"message": "Terjadi kesalahan saat menghubungi API Instagram!"}), 400
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"message": "Terjadi kesalahan pada server!"}), 500
    else:
        return jsonify({"message": "Code tidak ditemukan!"}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
