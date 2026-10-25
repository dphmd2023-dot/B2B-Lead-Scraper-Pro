import requests

print("=======================================================")
print(" 🎯 B2B Lead Scraper - Free CLI Demo (Limited to 5) ")
print(" 👉 Get Full GUI + Deep Email Crawler + Excel Export:")
print(" 🔗 https://tarmoun.gumroad.com/l/olpulz/LAUNCH40 ")
print("=======================================================\n")

city = input("Enter Target City (e.g., Paris, London, New York): ").strip() or "Paris"
print(f"\n[*] Searching sample leads in {city}...\n")

url = "https://nominatim.openstreetmap.org/search"
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, params={"q": f"restaurant in {city}", "format": "json", "limit": 5}, headers=headers).json()

for idx, item in enumerate(r, 1):
    print(f"[{idx}] {item.get('display_name')}")

print("\n=======================================================")
print("⚠️ DEMO LIMIT REACHED (5/5 Leads - No Emails/Excel)")
print("🚀 Unlock UNLIMITED Leads + Deep Website Email Scraper")
print("   + Bulk URL Extractor + 1-Click Excel/CSV GUI:")
print("👉 Download Pro Version (40% OFF Code: LAUNCH40):")
print("🔗 https://tarmoun.gumroad.com/l/olpulz/LAUNCH40")
print("=======================================================")
