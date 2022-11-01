import qrcode

# ID = input("Input ID\n")
# Name = input("Input Name\n")
filename = input("Input FileName\n")
# img = qrcode.make(f"{ID},{Name}")
img = qrcode.make("youtube.com")
image_path = "Downloads"
img.save(f"{image_path}/{filename}.jpg")
img.save(f"{image_path}/{filename}.jpg")
