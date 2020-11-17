#!/usr/bin/env python

import urllib
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import xmlrpclib
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import os
import sys
import glob
import re
import codecs

TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


class Custom_WP_XMLRPC:
    def post_article(self, wpUrl, wpUserName, wpPassword, articleCategories, path):
        self.path = path
        self.wpUrl = wpUrl
        self.wpUserName = wpUserName
        self.wpPassword = wpPassword

        client = Client(self.wpUrl, self.wpUserName, self.wpPassword)
        filename = self.path

        try:
            myFile = open(filename, "r")
            rawText = myFile.read()
            rawText = rawText.decode('latin-1')
            myFile.close()
            articleTitle = remove_tags(rawText)
            articleContent = rawText
            post = WordPressPost()
            post.title = articleTitle[:90]
            post.content = articleContent
            post.terms_names = {'category': articleCategories}
            post.post_status = 'publish'
            post.mime_type = "text/html"
            post.id = client.call(posts.NewPost(post))
            print ("success : " + os.path.basename(path))
            os.remove(path)
        except (Exception, e):
            print ("error : " + os.path.basename(path))
            print(e)


#########################################
# POST & Wp Credentials Detail #
#########################################

# Dont forget the /xmlrpc.php cause thats your posting adress for XML Server
wpUrl = 'https://chatwithtutor.com/xmlrpc.php'
# WordPress Username
wpUserName = ''
# WordPress Password
wpPassword = ''
# list of Categories
articleCategories = ['Homework']

#########################################
# Creating Class object & calling the xml rpc custom post Function
#########################################
xmlrpc_object = Custom_WP_XMLRPC()
# On Post submission this function will print the post id

print ("Directory: ", sys.argv[2])
files = glob.glob(sys.argv[2] + "/*.html")
for file in files:
    xmlrpc_object.post_article(wpUrl, wpUserName, wpPassword, articleCategories, file)
