from flask import Flask, request, jsonify

# Membuat instance dari aplikasi Flask
app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Permintaan verifikasi (GET)
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        # Cek apakah verify_token sesuai
        if verify_token == 'TOKEN_VERIFIKASI_KAMU':
            return challenge
        return 'Token verifikasi salah', 403

    # Permintaan webhook (POST)
    if request.method == 'POST':
        data = request.json
        print("Data Webhook Diterima:", data)

        # Ekstrak data komentar
        for entry in data.get("entry", []):
            for messaging in entry.get("messaging", []):
                comment_text = messaging.get("message", "")

                # Filter komentar berdasarkan kode yang tepat (misalnya "Kode_1")
                valid_comments = [
                    comment for comment in comment_text.split() if comment.strip() == "Kode_1"
                ]

                if valid_comments:
                    print(f"Komentar Valid Ditemukan: {valid_comments}")
                    print(f"Jumlah Komentar Valid: {len(valid_comments)}")
        
        return jsonify(status='received')

if __name__ == '__main__':
    # Menjalankan aplikasi Flask
    app.run(debug=True, port=5000)
