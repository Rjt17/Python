#!/usr/bin/env python

import pyPdf

f = open('TMR-Issue6.pdf','rb')

pdf = pyPdf.PdfFileReader(f)
pgs = pdf.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'

for pg in range(pgs):

    p = pdf.getPage(pg)
    o = p.getObject()

    if o.has_key(key):
        ann = o[key]
        for a in ann:
            u = a.getObject()
            if u[ank].has_key(uri):
                print (u[ank][uri])
