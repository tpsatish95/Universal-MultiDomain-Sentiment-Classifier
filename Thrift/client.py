# -*- coding: utf-8 -*-
from sentiments import Sentiments
from sentiments.ttypes import *
from sentiments.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import csv
import pickle

def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

'''
Arguments List:

general -> mainText,textType = "general"
microblogs -> mainText, textType = "microblogs"
comments -> mainText, textType = "comments"
reviews -> mainText, textType = "reviews", title = "" <optional>,topDomain,subDomain = "" <depends, not always optional, refer the list in config.py>
blogs_news -> mainText< or first paragraph>, title, textType="blogs_news",lastPara = "" <optional last paragraph>,middleParas = [] <optional middle paragraphs(separate each para with newline into string)>
'''

try:
	# Make socket
	transport = TSocket.TSocket('localhost', 8002)

	# Buffering is critical. Raw sockets are very slow
	transport = TTransport.TBufferedTransport(transport)

	# Wrap in a protocol
	protocol = TBinaryProtocol.TBinaryProtocol(transport)

	# Create a client to use the protocol encoder
	client = Sentiments.Client(protocol)

	# Connect!
	transport.open()

	client.ping()
	print ("ping()")

	writer = csv.writer(open("output.csv","w"))

	raw = load_obj("tweetDump")
	# raw = open("dataMultiSources.txt","r").readlines()
	for text in raw:
		# if "##" in text:
		# 	writer.writerow([text.replace("##","")," "])
		# else:
		text = text.strip()
		text = text.encode("utf-8")
		obj  = SentiRequestObject(text)
		senti = client.getSentimentScore(obj)
		print("The Text: "+ text)
		print(senti)
		writer.writerow([str(text),str(senti)])

	transport.close()

except Thrift.TException as tx:
  print ("%s" % (tx.message))
