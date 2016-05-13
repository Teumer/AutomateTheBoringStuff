#! python3
# backup_to_zip.py - Copies an entire folder and its content into
# a zip file whose filename increments

import os
import zipfile


def backup_to_zip(folder):
    """
    Backup the entire contents of "folder" into a ZIP file
    :param folder: string path to the folder whose contents should be backed up
    :return:
    """

    # Make sure the folder path is absolute
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on what files already exist
    number = 1
    zip_file_name = None
    while True:
        zip_file_name = os.path.basename(folder) + '_' + str(number) + ".zip"
        if not os.path.exists(zip_file_name):
            break
        number += 1

    # Create the ZIP file
    print("Creating {}...".format(zip_file_name))
    backup_zip = zipfile.ZipFile(zip_file_name, "w")

    # Walk the entire folder tree and compress the files in each folder
    for main_name, sub_name, file_name in os.walk(folder):
        print("Adding files in {}".format(main_name))

        # Add the current folder to the ZIP file
        for filename in file_name:
            new_base = os.path.basename(folder) + "_"

            # Don't backup the backup ZIP files
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(main_name, filename))

    backup_zip.close()
    print("Done.")
