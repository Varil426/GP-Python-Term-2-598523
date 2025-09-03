imiona = ["Bartek", "Leonard"]
nazwiska = ["Kręgielewski", "R"]
wiek = [26, 13]

# Wyświetlanie
for i in range(len(imiona)):
    print(imiona[i], nazwiska[i])
    if (wiek[i] >= 18):
        print(f"{imiona[i]} ma {wiek[i]} lat, jest pełnoletni")
    else:
     print(f"{imiona[i]} ma {wiek[i]} lat, nie jest pełnoletni")