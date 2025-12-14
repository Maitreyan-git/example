import qrcode
from PIL import Image

def create_qr_code(data, fill_color="black", back_color="white", logo_path=None, save_path="my_qr.png"):
    # Create basic QR Code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    # Add logo (optional)
    if logo_path:
        try:
            logo = Image.open(logo_path)
            logo_size = 80  # adjust as needed
            logo = logo.resize((logo_size, logo_size))

            # Positioning logo in the center
            pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)
        except Exception as e:
            print(f"Error adding logo: {e}")

    # Save the final QR code
    img.save(save_path)
    print(f"✅ QR Code saved as {save_path}")

# ---- Run the function with user input ----
if __name__ == "__main__":
    user_data = input("Enter the text or URL for your QR code: ")
    color = input("Enter the color of the QR (default black): ") or "black"
    bg_color = input("Enter the background color (default white): ") or "white"
    logo_file = input("Enter path to logo image (or leave blank): ") or None

    create_qr_code(user_data, fill_color=color, back_color=bg_color, logo_path=logo_file)
