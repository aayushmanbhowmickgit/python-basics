import qrcode

# Ask the user what they want to put in the QR code
data = input("Enter text or URL: ")

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code
img.save(data.replace(" ", "_") + "_qr_code.png")

print("QR code created successfully!")
print("Saved as: " + data.replace(" ", "_") + "_qr_code.png")
