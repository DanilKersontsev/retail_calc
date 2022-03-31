print("kui sooritate ostu mis on rohkem või võrdne 5000$ saate lisa soodustust")
kauba_valik = input("sisestage kaup mida soovite osta: ")
kauba_kogus = int(input("Sisestage kauba kogus: "))
asukoht = input("Sisestage State: ").upper()

esialgne_kauba_hind = kauba_kogus
print( "kauba alghind on",esialgne_kauba_hind, "$",)

if kauba_kogus >= 1000 and kauba_kogus < 5000:
    discounted_hind =  kauba_kogus - (kauba_kogus * 0.03)
    taxed_hind = (discounted_hind * float(asukoht) + discounted_hind)
    print("Kogusumma koos soodustuse ja maksudega" ,taxed_hind, "$")

