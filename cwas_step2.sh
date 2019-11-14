
singimage=/data/joy/BBL/applications/bids_apps/cwasmdmr2.simg # cwasmdmr image on chead
scriptdir=/usr/local/bin # script to run inside the image


mdmrouput=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/output #output directory. note that i added /home/username in front
brainmask=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/MNIgreymask4mm.nii.gz #brainmask usually greymatter mask
bgim=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/MNIgreymask4mm.nii.gz #usually pnc template

imagelist=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/cwasnifti.csv  # list of image in nifti # check image list, /home/username

modelcsv=/home/ddavila//data/jux/BBL/projects/grmpy-restbold/subs/model_transformed.csv # demographic and factors,
##
#rm  -rf $mdmrouput # remove previous run if exist



formula='ari_avg_transform+sex+age+restRelMeanRMSMotion' # formula
factor1='ari_avg_transform' # factor to permute 1.e the main factor
/share/apps/singularity/2.5.1/bin/singularity exec -e -B /data:/home/ddavila/data $singimage  $scriptdir/Rscript $scriptdir/connectir_mdmr.R \
       --indir=$mdmrouput \
    --formula="$formula" \
    --model=$modelcsv \
    --factors2perm=$factor1 \
    --save-perms --ignoreprocerror \
     logk_sex_age
