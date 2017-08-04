# htcondor_test
testing htcondor at cern

Make sure to initialize the FCC software stack in the usual way, for the latest version of the software.
e.g.:

    source /cvmfs/fcc.cern.ch/sw/0.8.1/init_fcc_stack.sh

submit:

    condor_submit multiple.sub

check your jobs:

    condor_q

check that you are using the fcc accounting group: 

    condor_q -long | grep AccountingGroup

should give something like:

```
[python_toy]$ condor_q -long | grep AccountingGroup
AccountingGroup = "group_u_FCC.local_gen.cbern"
...
```

Further information about htcondor: 
- A much better tutorial than the one of CERN! http://research.cs.wisc.edu/htcondor/tutorials/intl-grid-school-3/submit_first.html
- Condor documentation: https://research.cs.wisc.edu/htcondor/manual/

