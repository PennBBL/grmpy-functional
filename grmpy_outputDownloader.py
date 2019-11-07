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

            print (y.label)

            #Download the entire output
            outname = 'ses-{}.zip'.format(sessions[x].label)
            y.download_file('xcpEngineouput_xcp.zip', outname)

            # Copy the important sutuff
            with zipfile.ZipFile(outname,"r") as zip_ref:
                zip_ref.extractall('xcpengine')


            folder = "sub-{}".format(sessions[x].subject.label)

            os.system("mkdir {}".format(folder))
            os.system('cp xcpengine/xcpengine/*/*/task-rest/acq-singleband/*csv {}'.format(folder))
            os.system("cp xcpengine/xcpengine/*/*/task-rest/acq-singleband/*html {}".format(folder))
            os.system("cp xcpengine/xcpengine/*/*/task-rest/acq-singleband/*csv {}".format(folder))
            os.system("cp -r xcpengine/xcpengine/*/*/task-rest/acq-singleband/roiquant {}".format(folder))
            os.system("cp -r xcpengine/xcpengine/*/*/task-rest/acq-singleband/reho {}".format(folder))
            os.system("cp -r xcpengine/xcpengine/*/*/task-rest/acq-singleband/alff {}".format(folder))
            os.system("cp -r xcpengine/xcpengine/*/*/task-rest/acq-singleband/figures {}".format(folder))
            os.system("cp xcpengine/xcpengine/*/*/task-rest/acq-singleband/norm/*_task-rest_acq-singleband_maskStd.nii.gz {}".format(folder))
            os.system("cp xcpengine/xcpengine/*/*/task-rest/acq-singleband/norm/*task-rest_acq-singleband_img_sm6Std.nii.gz {}".format(folder))

            # Get rid of junk
            os.system('rm {}'.format(outname))
            os.system('rm -r xcpengine')
