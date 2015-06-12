#!/usr/bin/env python

import os
import sys

#rootDir = "bower_components"

numArgs = len(sys.argv)

if numArgs <= 1:
    print 'usage: get_all_imports.py <bower_components directory> [prefix (default "..")]'
    exit(1)

rootDir = sys.argv[1]

if not (rootDir == "bower_components" or rootDir == "components"):
    print 'Cowardly refusing to search non bower directory "' + rootDir + '"'
    exit(1)

bowerPrefix = ".."
if numArgs >= 3:
    bowerPrefix = sys.argv[2]

def shouldInclude(f, path):
    blacklisted = ['src', 'demo', 'test', 'polymer', 'web-animations']
    for blacklist in blacklisted:
        if blacklist in path: return False
    fileName, extension = os.path.splitext(f)
    return extension == ".html" and fileName != "index"

def getImports(dir):
    imports = []
    for root, dirs, files in os.walk(dir):
        path = root.split('/')
        prefix = os.path.join(bowerPrefix, root)
#        print (len(path) - 1) *'---' , os.path.basename(root)
        for file in files:
            if shouldInclude(file, prefix):
                i = os.path.join(prefix, file)
#                print "adding import: ", i
                imports.append(i)
    return imports

def tagify(i):
    importTag = '<link rel="import" href="' 
    importTerminator = '">'
    return importTag + i + importTerminator

def htmlify(imports):
    html = []
    for i in imports:
        html.append(tagify(i))
    return html

# polymer is special
polymer = os.path.join(bowerPrefix, rootDir, "polymer/polymer.html")

def printHtml(html):
    print tagify(polymer)
    for tag in html:
        print tag

imports = getImports(rootDir)
html = htmlify(imports)

printHtml(html)
