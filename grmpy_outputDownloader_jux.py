# Setup and Imports
import zipfile
import os
import flywheel
fw = flywheel.Client()
proj = fw.projects.find_first('label=GRMPY_822831')
sessions = proj.sessions()
sessions = [fw.get(x.id) for x in sessions]

# Download and Clear Loop
for x in range(len(sessions)):
    for y in sessions[x].analyses:
        if 'XCP_resting_36despike' in y.label: # Only download the desired XCP output

            #print (y.label)

            #Download the entire output
            outname = '/data/jux/BBL/projects/diego_cwasPractice/subs/ses-{}.zip'.format(sessions[x].label)
            y.download_file('xcpEngineouput_xcp.zip', outname)
            os.system('unzip   ' + outname + ' -d /data/jux/BBL/projects/diego_cwasPractice/subs/ ')

            # Copy the important sutuff
            #with zipfile.ZipFile(outname,"r") as zip_ref:
                #zip_ref.extractall('xcpengine')


            folder = "/data/jux/BBL/projects/diego_cwasPractice/subs/sub-{}".format(sessions[x].subject.label)

            os.system('mkdir  ' + folder)
            os.system('cp /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/*csv  ' + folder)
            os.system('cp /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/*html ' + folder)
            os.system('cp /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/*csv ' + folder)
            os.system('cp -r /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/roiquant ' + folder)
            os.system('cp -r /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/reho ' + folder)
            os.system('cp -r /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/alff ' + folder)
            os.system('cp -r /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/figures ' + folder)
            os.system('cp /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/norm/*_task-rest_acq-singleband_maskStd.nii.gz ' + folder)
            os.system('cp /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine/*/*/task-rest/acq-singleband/norm/*task-rest_acq-singleband_img_sm6Std.nii.gz ' + folder)

            # Get rid of junk
            os.system('rm  ' + outname )
            os.system('rm -r /data/jux/BBL/projects/diego_cwasPractice/subs/xcpengine')
