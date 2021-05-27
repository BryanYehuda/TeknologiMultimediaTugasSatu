from PIL import Image #library image

mode_to_bpp = {'1':1, 'L':8, 'P':8, 'RGB':24, 'RGBA':32, 'CMYK':32, 'YCbCr':24, 'I':32, 'F':32} #array mode ke bit per pixel
data = Image.open('test.jpg') #membuka gambar
bpp = mode_to_bpp[data.mode] #mendapatkan mode gambar
pic_rgb = data.convert("RGB") #melakukan convert gambar ke rgb
width, height = data.size #mendapatkan panjang dan lebar gambar

print ("\nJumlah bit per pixel (bit depth) : \n" + str(bpp)) #print jumlah bit per pixel

print ("\nNilai tiap pixel : ") 
for x in range (width) : #looping lebar
 for y in range (height) : #looping tinggi
    rgb_pixel_value = pic_rgb.getpixel((x,y)) #mendapat niai rgb di pixel yang sedang di loop
    print(rgb_pixel_value, end =" ") #print nilai RGB
print ("\n\nTotal jumlah pixel : \n" + str(width*height) +"\n") #print total jumlah pixel