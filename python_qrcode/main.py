import qrcode

# Create a QR code object with configuration
qr = qrcode.QRCode(
    version=1,       # Smallest version (21x21 pixels)
    box_size=10,     # Size of each "box" in the QR code
    border=5,        # Thickness of the quiet zone around the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L  # Lowest error correction level (7%)
)

# Add the data to be encoded in the QR code (your GitHub URL)
data = "https://github.com/kingpin147"
qr.add_data(data)

# Generate the QR code data
qr.make(fit=True)  # Ensure the data fits within the specified version/size

# Create an image of the QR code with specified colors
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
img.save("github.png")  
