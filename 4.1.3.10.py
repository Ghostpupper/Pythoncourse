def l100kmtompg(liters):
    gallon = liters * 3.785411784
    # gallons/100km
    x = 1 / gallon
    # 100km/gallons
    x *= 0.01609344

    return x


def mpgtol100km(miles):
    liters = miles / 3.785411784
    x = 1 / liters
    x /= 0.01609344

    return x


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))