import qrcode as qr

data = 'https://wonderworlddigital.com/wwd022.html'

# Encoding data using make() function
img = qr.make(data)

# Saving as an image file
img.save('mayan.png')

# import json
# import qrcode as qr

# # Load the JSON data
# with open('./100_guest.json', 'r') as file:
#     data = json.load(file)

# # Assuming your JSON structure is a list of dictionaries with an 'id' key:
# # Example: [{"id": "https://example1.com"}, {"id": "https://example2.com"}, ...]
# for index, item in enumerate(data, start=1):
#     img = qr.make(item['id'])
#     img.save(f'{index}.png')