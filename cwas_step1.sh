
singimage=/data/joy/BBL/applications/bids_apps/cwasmdmr2.simg # cwasmdmr image on chead
scriptdir=/usr/local/bin # script to run inside the image


mdmrouput=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/output #output directory. note that i added /home/username in front
brainmask=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/MNIgreymask4mm.nii.gz #brainmask usually greymatter mask
bgim=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/MNIgreymask4mm.nii.gz #usually pnc template

imagelist=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/cwasnifti.csv  # list of image in nifti # check image list, /home/username

##

#rm  -rf $mdmrouput # remove previous run if exist
metric=pearson # pearson correllation

# compute distance matrix

/share/apps/singularity/2.5.1/bin/singularity exec -e -B /data:/home/ddavila/data $singimage $scriptdir/Rscript $scriptdir/connectir_subdist.R \
       $mdmrouput \
       --infuncs1=$imagelist \
       --ztransform \
       --automask1  -c 3 -t 4 \
       --brainmask1=$brainmask \
       --method="$metric"  \
       --bg=$bgim   --overwrite \
       --memlimit=30
