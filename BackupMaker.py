import os, shutil
from DirDialogBox import loc_browser

if os.path.isdir('SuccessfulBackup') == False: # creates the SuccessfulBackup directory if not already created
    os.makedirs('SuccessfulBackup')

suc_backup = os.path.join(os.getcwd(), 'SuccessfulBackup')

if os.path.isfile('bulocks.txt') == False: # this creates backup location (bulocks) txt file if not already created and add the first backup location through dialog box 
    print('No backup location found, please select one')
    added_loc = loc_browser()              # opens directory browser and creates/modify the bulocks text file
    print('Added new location: ',added_loc)

def read_bulocks():
    global list_loc
    list_loc = []
    with open('bulocks.txt', 'r') as locations: # the txt file is read and each location is added to the list- list_loc
        for each_location in locations:
            list_loc.append(each_location)

    list_loc = [x.strip() for x in list_loc] # this removes the escape characters from location string

def backup_process():
    for each_file in os.listdir(): # this now goes through each file to take back up
        if each_file == 'SuccessfulBackup' or each_file == 'BackupMaker.py' or each_file == 'bulocks.txt' or each_file == 'DirDialogBox.py' or each_file == 'BackupMaker.exe' or each_file == '__pycache__':
            continue
        print(each_file)
        for each_loc in list_loc:
            if os.path.isfile(each_file) == True:
                shutil.copy(each_file, each_loc)
            else:
                try:
                    shutil.copytree(each_file, os.path.join(each_loc, each_file))
                except FileExistsError:
                    shutil.rmtree(os.path.join(each_loc, each_file))
                    shutil.copytree(each_file, os.path.join(each_loc, each_file))
        
        file_loc = os.path.join(os.getcwd(), each_file)          # this gets the actual location of each file
        dest_loc = os.path.join(suc_backup, each_file)           # this genrates the destination location  
        os.replace(file_loc, dest_loc)                           # this moves the files to SuccessfulBackup directory once the backup is made

def re_backup(new_loc):

    for each_file in os.listdir(suc_backup): # this now goes through each file to take back up
        original_loc = os.path.join(suc_backup, each_file) 
        if os.path.isfile(original_loc) == True:
            shutil.copy(original_loc, new_loc)
        else:
            try:
                shutil.copytree(original_loc, os.path.join(new_loc, each_file))
            except FileExistsError:
                shutil.rmtree(os.path.join(new_loc, each_file))
                shutil.copytree(original_loc, os.path.join(new_loc, each_file))

def instruction():
    print('************************************************************************')
    print('For Creating backup press 1\nFor adding new back up location press 2\nTo exit press 3\n')

instruction()

while True:
    user_input = input()
    if user_input == '1': # proceed to backup
        read_bulocks()
        if not list_loc:
            print('No backup location found, please select one') # if bulocks is empty
            loc_browser() # opens directory browser and creates/modify the bulocks text file
            instruction()
            continue
        backup_process()
        print('Back up completed!')

    if user_input == '2': # if 2 then new location is added in the bulocks txt file
        new_loc = loc_browser() # opens directory browser and creates/modify the bulocks text file
        print('Added new location: ', new_loc)
        user_input2 = input('Do you want to make whole backup again in this new location? (y/n): ')
        if user_input2.lower() == 'y':
            re_backup(new_loc=new_loc)
            print('Back up completed!')
        else:
            print('Back up aborted!')
    instruction()
    if user_input == '3': # exit
        break