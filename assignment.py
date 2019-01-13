import pydicom
import os
file=open("Output1.txt","a")
ds = pydicom.dcmread("ttfm.dcm")
for i in ds.dir():
    file.write(i+"\n")
ds = pydicom.dcmread("bmode.dcm")
for i in ds.dir():
    file.write(i+"\n")
file.close()