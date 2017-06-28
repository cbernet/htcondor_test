#!/bin/env python
import sys
import os 
import shutil

args = sys.argv[1:]

if len(args)!=3:
    print 'usage cluster_id process_id a_value'
    sys.exit(1)

cluster_id, process_id, value = args

dirname = 'output_{}_{}'.format(cluster_id, process_id)
if os.path.isdir(dirname):
    shutil.rmtree(dirname)
os.mkdir(dirname)
output = open( dirname+'/toto.txt', 'w')
output.write(value)
output.write('\n')
output.close()

print dirname, 'created'

