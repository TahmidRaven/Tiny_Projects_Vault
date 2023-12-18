import os
import qrcode


output_directory = "C:/CODE/TahmidRaven/Tiny_Projects_Vault/QR_Code_Generator/images"
os.makedirs(output_directory, exist_ok=True)

makeQR = input("Enter the link that you want to generate:")
filename = input("Enter the name of your QR code (including extension, e.g., qrcode.jpg): ")

if not filename.endswith((".jpg", ".png", ".gif")):
    filename += ".jpg"

myqr = qrcode.QRCode(version=1,
                     error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=10,
                     border=4)

# myqr.add_data("https://github.com/TahmidRaven")
myqr.add_data(makeQR)

img = myqr.make_image(fill_color="#422F90", back_color="white")  

# hexcode blade runner 2049:  #932F8C #441d4b #422F90 

img.save(os.path.join(output_directory, filename))
