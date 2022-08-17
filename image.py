
def image_resize_append():

  from PIL import Image

  image_paths = [
      'D:\\Github\\Aktien\\Output\\Bitcoin-EUR.png', 
      'D:\\Github\\Aktien\\Output\\HSBC MSCI World ETF.png',
      'D:\\Github\\Aktien\\Output\\Lufthansa.png',
      'D:\\Github\\Aktien\\Output\\crude oil.png'
      ]


  images = [Image.open(x) for x in image_paths]
  widths, heights = zip(*(i.size for i in images))

  # resizing images
  i=0
  for im in images:
    new_width = 1920
    new_height = int(new_width / im.width * im.height)
    print(new_height)
    new_size = im.resize((new_width, new_height))
    new_size.save(image_paths[i])
    i=i+1

  images = [Image.open(x) for x in image_paths]
  widths, heights = zip(*(i.size for i in images))

  max_width = max(widths)
  total_height = sum(heights)

  new_im = Image.new('RGB', (max_width, total_height))

  y_offset = 0
  for im in images:
    new_im.paste(im, (0, y_offset))
    y_offset += im.size[1] +42

  new_im.save('D:\\Github\\Aktien\\Output\\test.png')
  print("fertig :)")

  new_im = Image.open(r'D:\\Github\\Aktien\\Output\\test.png')
  im_1 = new_im.convert('RGB')
  im_1.save(r'D:\\Github\\Aktien\\Output\\test.pdf')

