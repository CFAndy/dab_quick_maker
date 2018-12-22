from lxml import etree
import shutil
import os
from os import path
class SoundResource:
    pass

def add_sub_element(parent, name, value = None):
    sub_node = etree.SubElement(parent, name)
    if value:
        sub_node.text = value
    return sub_node


sound_path = r"D:\早教\rip\letterland\level2-1-cd2\letterland-level2-a-proj\sound"
image_path = r"D:\早教\rip\letterland\level2-1-cd2\letterland-level2-a-proj\images"
image_src = r"D:\早教\rip\letterland\level2-1-cd2\letterland-level2-a-proj\images\20181222152100.jpg"
image_id = 20181222152100
bookinfo = etree.Element('bookinfo')
doc = etree.ElementTree(bookinfo)
page_id = 1
mp3_files = os.listdir(sound_path)
mp3_files.pop(0)

for x in mp3_files:
    image_info = etree.SubElement(bookinfo, 'imageinfo')
    name =  str(image_id)+".jpg"
    image_tgt = os.path.join(image_path, name)
    if not os.path.exists(image_tgt):
        print("copy {} {} ".format(image_src, image_tgt))
        shutil.copyfile(image_src, image_tgt)
    add_sub_element(image_info, "name", name)
    add_sub_element(image_info, "remark", "new page")
    add_sub_element(image_info, "edited")
    add_sub_element(image_info, "zoomoutby")
    add_sub_element(image_info, "zoomoutnum")
    add_sub_element(image_info, "public")
    oid = add_sub_element(image_info, "oid")
    add_sub_element(oid, "oidnum", "{0:04d}".format(page_id))
    add_sub_element(oid, "pointx", "347")
    add_sub_element(oid, "pointy", "35")
    add_sub_element(oid, "sound", x)
    page_id = page_id + 1
    image_id = image_id + 1
doc.write("bookinfo.xml", pretty_print=True)
