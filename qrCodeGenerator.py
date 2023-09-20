import qrcode as qr

data = 'https://wonderworlddigital.com/wwd021.html'

# Encoding data using make() function
img = qr.make(data)

# Saving as an image file
img.save('mayan.png')