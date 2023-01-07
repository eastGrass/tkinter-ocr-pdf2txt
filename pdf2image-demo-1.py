# import module
import os
import sys
import string
from pdf2image import convert_from_path

"""
this program convert a specific pdf file into iamges.

Args:
srcPath - the absolute path of source pdf file
destDir - the destination dir

Returns: none

Raises:
KeyError - raises an exception
"""
def pdf2image_demo(srcPath: string, destDir: string):
    # Store Pdf with convert_from_path function

    # verify the in parameters
    # srcPath exist and this file is the pdf type
    if not os.path.isfile(srcPath):
        raise RuntimeError('the source path should be a file')

    _, file_extension = os.path.splitext(srcPath)
    if (file_extension.lower() != '.pdf'):
        raise RuntimeError('the source file should be a pdf file')

    if not os.path.exists(destDir):
        os.makedirs(destDir) # 创建目录

    images = convert_from_path(srcPath)
    for i in range(len(images)):
    
        # Save pages as images 
        images[i].save(destDir + '\\'+ 'page'+ str(i) +'.jpg', 'JPEG')

if __name__== "__main__" :
    print("format: python pdf2image-demo-1 srcFilePath destDir")
    for i in range(len(sys.argv)):
        print(sys.argv[i])

    pdf2image_demo(sys.argv[1], sys.argv[2])