#22
#15.01.2025 Marii


from datetime import datetime, timedelta

sp = datetime(1989, 11, 6)
now = datetime.now()
print(now)
print(now.strftime("%d.%m.%d %H:%M:%S"))

# Arvuta nende kahe kuupäeva vahe
difference = now - sp

print("Kuupäevade vahe päevades:", difference.days)



