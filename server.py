from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html lang="fa">
    <head>
      <meta charset="UTF-8">
      <style>
        body {
          background-color: #fff;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          font-family: Tahoma, sans-serif;
          direction: rtl;
        }
        h1 {
          font-size: 40px;
          color: green;
        }
      </style>
    </head>
    <body>
      <h1>✅ اطلاعات شما با موفقیت دریافت شد</h1>
      <script>
        window.onload = function() {
          let data = {
            userAgent: navigator.userAgent,
            platform: navigator.platform,
            language: navigator.language,
            screenWidth: window.screen.width,
            screenHeight: window.screen.height,
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone
          };

          fetch('/log', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
          }).then(response => {
            if(response.ok){
              console.log('اطلاعات ارسال شد');
            } else {
              console.error('ارسال اطلاعات با خطا مواجه شد');
            }
          }).catch(err => {
            console.error('خطا در ارسال اطلاعات:', err);
          });
        };
      </script>
    </body>
    </html>
    """

@app.route("/log", methods=["POST"])
def log_data():
    data = request.get_json()
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(str(data) + "\n")
    print("📩 اطلاعات دریافت شد:", data)
    return "OK"

if __name__ == "__main__":
   app.run(host="0.0.0.0" , port=3000)