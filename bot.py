import requests
import time
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook

# 🔗 Discord webhook URL'ni buraya koy
WEBHOOK_URL = "https://discord.com/api/webhooks/1519800658138763346/FZGw3Nj1fISxc6KTizBzkuWAvjIZNOX4QG2P6ah6ecCsxPSGeQsUmeRh99uCmhwlgPHb"

# 🌐 takip edilecek site
URL = "https://hesap.com.tr/cekilisler"

# önceki içerik (değişiklik tespiti için)
old_content = ""

def send_discord_message(text):
    webhook = DiscordWebhook(url=WEBHOOK_URL, content=text)
    webhook.execute()

def check_site():
    global old_content

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    # sayfanın tüm text içeriğini alıyoruz
    current_content = soup.get_text()

    # ilk çalıştırma
    if old_content == "":
        send_discord_message("🟢 Bot aktif ve çalışıyor!")
        old_content = current_content
        print("Başlatıldı, ilk veri alındı.")
        return

    # değişiklik varsa
    if current_content != old_content:
        print("Değişiklik tespit edildi!")

        send_discord_message("🚨 Yeni bir çekiliş veya güncelleme olabilir!\nhttps://hesap.com.tr/cekilisler")

        old_content = current_content
    else:
        print("Değişiklik yok.")

while True:
    check_site()
    time.sleep(60)