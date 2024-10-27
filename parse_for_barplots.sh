#!/usr/bin/bash

awk 'NR==1' uls-a1-avg-mat-tr.dat > 1ulsnew-chol.dat
awk 'NR==1' uls-a1-avg-err-tr.dat >> 1ulsnew-chol.dat
awk 'NR==2' uls-a1-avg-mat-tr.dat > 1ulsnew-dpsm.dat
awk 'NR==2' uls-a1-avg-err-tr.dat >> 1ulsnew-dpsm.dat
awk 'NR==3' uls-a1-avg-mat-tr.dat > 1ulsnew-dpg1.dat
awk 'NR==3' uls-a1-avg-err-tr.dat >> 1ulsnew-dpg1.dat
awk 'NR==4' uls-a1-avg-mat-tr.dat > 1ulsnew-sdpe.dat
awk 'NR==4' uls-a1-avg-err-tr.dat >> 1ulsnew-sdpe.dat
awk 'NR==5' uls-a1-avg-mat-tr.dat > 1ulsnew-popc.dat
awk 'NR==5' uls-a1-avg-err-tr.dat >> 1ulsnew-popc.dat
awk 'NR==6' uls-a1-avg-mat-tr.dat > 1ulsnew-dppc.dat
awk 'NR==6' uls-a1-avg-err-tr.dat >> 1ulsnew-dppc.dat
awk 'NR==7' uls-a1-avg-mat-tr.dat > 1ulsnew-sopc.dat
awk 'NR==7' uls-a1-avg-err-tr.dat >> 1ulsnew-sopc.dat
