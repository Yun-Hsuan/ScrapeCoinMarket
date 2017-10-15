from utils import *
import os,sys
from multiprocessing import Process


if len(sys.argv) < 2 :
    print ("args:  <pair file>")
    exit(1)
    
pairs, date_begin_str, date_end_str, period= Parser(sys.argv[1])

#exit(1)
aval_pairs = get_pair_names()


## Tilt
Queue = []
for pair in pairs:
	print (pair)
	if pair in aval_pairs:
		Queue.append( Process( target=scrpe_trade_history, args=(pair,date_end_str,date_begin_str,period) ) )

## launch parallel
for proc in Queue:
	proc.start()


## Synchronize:
for proc in Queue:
	proc.join()


print ("All done.")
exit(1)

