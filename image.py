
def image_resize_append(image_paths):

  from PIL import Image

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

  anzahlCharts= len(image_paths)
  OffsetZwischenCharts = 10
  summeOffset = anzahlCharts * OffsetZwischenCharts

  max_width = max(widths)
  total_height = sum(heights) + summeOffset

  new_im = Image.new('RGB', (max_width, total_height))

  y_offset = 0
  for im in images:
    new_im.paste(im, (0, y_offset))
    y_offset += im.size[1] + OffsetZwischenCharts

  new_im.save('D:\\Github\\Aktien\\Output\\test.png')
  print("fertig :)")

  new_im = Image.open(r'D:\\Github\\Aktien\\Output\\test.png')
  im_1 = new_im.convert('RGB')
  im_1.save(r'D:\\Github\\Aktien\\Output\\test.pdf')

