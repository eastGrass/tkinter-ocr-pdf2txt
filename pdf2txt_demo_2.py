import os
import sys
import shutil
import string
from tempfile import mkdtemp
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

"""
this program convert a specific pdf file into txt file.

Args:
srcPath - the absolute path of source pdf file
destDir - the destination dir of txt file
ocrEng - the path of ocr engine

Returns: none

Raises:
KeyError - raises an exception
"""
def pdf2txt_demo(srcPath: string, destTxtDir: string, ocrEng: string):
    contents = []
    # orc engine
    pytesseract.pytesseract.tesseract_cmd = ocrEng

    # print("in = %s"%(srcPath))
    # print("out = {0}".format(destTxtDir))
    # print("config = {0}".format(ocrEng))

    # pdf -> imgs
    if not os.path.isfile(srcPath):
        raise RuntimeError('the source path should be a file')

    # 分离出 文件路径 + 文件名 + 文件后缀(类型)
    srcFilePath, fileNameExt=  os.path.split(srcPath)
    fileName, file_extension = os.path.splitext(fileNameExt)
    if (file_extension.lower() != '.pdf'):
        raise RuntimeError('the source file should be a pdf file')

    images = convert_from_path(srcPath)
    for i in range(len(images)):        
        # Save pages as images for each page
        item =  images.pop(0)
 
        if item != None:
            # imgs -> txt
            page_content = pytesseract.image_to_string(item, lang='chi_sim+equ+eng')
            contents.append(page_content)    

            del item  

    
    # txt filename
    if destTxtDir == "":
        destTxtDir = srcFilePath 
    else:
        if not os.path.exists(destTxtDir):
            os.makedirs(destTxtDir)

    destFile = os.path.join(destTxtDir,  fileName + ".txt")

    # write txt
    with open(destFile, 'w', encoding='utf-8') as f_out:
        f_out.write(''.join(contents))
 



if __name__== "__main__" :
    print("format: python pdf2txt-demo-1 srcFilePath destDir")
    
    orcEngPath = r'D:\Program Files\Tesseract-OCR\tesseract.exe'

    pdf2txt_demo(sys.argv[1], sys.argv[2], orcEngPath)
