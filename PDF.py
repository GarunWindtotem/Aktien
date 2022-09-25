
# def pdf_erstellen(imagelist):

#     from fpdf import FPDF
#     pdf = FPDF()
#     # imagelist is the list with all image filenames
#     imagelist = [
#         "D:\\Github\\Aktien\\Output\\Bitcoin-EUR.png", 
#         "D:\\Github\\Aktien\\Output\\HSBC MSCI World ETF.png", 
#         "D:\\Github\\Aktien\\Output\\Lufthansa.png"
#         ]

#     for image in imagelist:
#         pdf.add_page()
#         pdf.image(image,10,10,594, 420)
#     pdf.output("D:\\Github\\Aktien\\Output\\yourfile.pdf", "F")

#     print("fertig :D")

#     return