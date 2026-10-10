import json
import urllib.error
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

UCET = "8ce7addfe0b78a5b7b53efc5b32bb9dd"
DATABAZE = "c6c30bd3-6c00-49a6-a6cb-e364cd33b8c7"
token = input("Token: ").strip()

adresa = f"https://api.cloudflare.com/client/v4/accounts/{UCET}/d1/database/{DATABAZE}/query"
hlavicky = {"Authorization": "Bearer " + token, "Content-Type": "application/json"}


def sql(prikaz, hodnoty=()):
    telo = json.dumps({"sql": prikaz, "params": list(hodnoty)}).encode("utf-8")
    pozadavek = urllib.request.Request(adresa, data=telo, headers=hlavicky, method="POST")
    try:
        with urllib.request.urlopen(pozadavek, timeout=20) as odpoved:
            data = json.loads(odpoved.read())
    except urllib.error.HTTPError as chyba:
        print("Cloudflare odmítl požadavek, HTTP", chyba.code)
        print(chyba.read().decode("utf-8", "replace")[:400])
        raise SystemExit(1)
    return data["result"][0]["results"]


print("Hráči:")
for radek in sql("SELECT id, prezdivka, vytvoren FROM hrac"):
    print(f"  {radek['id']:>3}  {radek['prezdivka']:<12} {radek['vytvoren']}")

print()
print("Žebříček:")
dotaz = """
    SELECT hrac.prezdivka, skore.body, skore.uroven
    FROM skore JOIN hrac ON hrac.id = skore.id_hrace
    ORDER BY skore.body DESC LIMIT 5
"""
for radek in sql(dotaz):
    print(f"  {radek['prezdivka']:<12} {radek['body']:>6}  úroveň {radek['uroven']}")