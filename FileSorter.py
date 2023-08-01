#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Import the modules
import os
import shutil
import logging
import argparse


# In[25]:


def convert_list_to_lowercase(myList):
    """
    This function takes a list and convert it to lowercase.
    
    Parameters:
        myList (list): The list you want to convert to lowercase.
        
    Returns:
        list: the lowercase list.
    """
    return [x.lower() for x in myList]


# In[26]:


def get_file_extention(name):
    """
    This function take a filename and returns the extention/type of the file.
    
    Parameters:
        name (string): The the name of the file with its extension.
        
    Returns:
        string: The extension/type of the file
    """
    filename = os.path.splitext(name)[1]
    if filename == '':
        return "folder"
    else:
        return filename


# In[33]:


def read_extensions_from_file(filename):
    """
    This function take a .txt filename that contains file extensions and returns them all as list.
    
    example:
        read_extensions_from_file("image_extensions.txt")
        
        the .txt file should look like this:
            .APNG
            .AVIF
            .GIF
            ...
    
    Parameters:
        filename: (string): the name of the file with its extension
        
    Returns:
        list: A list of all the extensions
    
    """
    extensions = []

    try:
        with open(filename, 'r') as f:
            for line in f:
                extension = line.strip()
                extensions.append(extension)
        
        logging.debug(f"All the extensions from {filename} file have been read successfully")
    except FileNotFoundError as e:
        logging.error(f"File not found: {filename}")
    except Exception as e:
        logging.error(f"Error reading extensions from {filename}: {e}")

    return extensions


# In[45]:


def directory_check(directory):
    """
    This function take a directory and check if the given directory exist or is empty.
    If the given directory exis or is empty, it terminates the program.
    
    example: 
        directory_check("C:\your\path\here\") 
    
    Parameters:
        directory: (string): the directory path
    
    """
    if not os.path.exists(directory):
        print("The directory does not exist.")
        exit(1)

    if not os.listdir(directory):
        print("The folder is empty.")
        exit(1)

    # If both conditions are met, the directory is valid and not empty
    print("Directory is valid and not empty.")
    # Add any additional actions you want to perform here


# In[ ]:


def create_backup(directory):
    """
    This function creates a backup for the given directory.
    Note that it does't backup the folders, only the files in the directory.
    
    example: 
        create_backup("C:\your\path\here\") 
        
    Parameters:
        directory: (string): the directory path
    """
    logging.debug(f"creating backup")
    print("\n---------- CREATING BACKUP ----------n")
    files = os.listdir(directory)
    try:
        # create a backup folder
        os.mkdir(directory + "\\FileSorter_backup")
        print("Created FileSorter_backup folder")
        logging.debug(f"Created 'FileSorter_backup' folder at: {os.path.join(directory, 'FileSorter_backup')}")
        backup_folder = "FileSorter_backup"
    except OSError as e:
        print(f"Error creating the 'FileSorter_backup' folder: {e}")
        logging.error(f"Error creating the 'FileSorter_backup' folder:: {e}")
        exit(1)
        
    # Move the files the backup folder
    for file in files:
        file_extension = get_file_extention(file)
        # if the file is not a folder
        if file_extension != "folder":
            # select the file   
            file_to_move = os.path.join(directory, file)

            # select the directory
            destination = os.path.join(directory, backup_folder)

            try:
                # move the file to the specified directory
                shutil.copy(file_to_move, destination)
                print(f"Moving {file_to_move} to {destination}")
                logging.debug(f"Moving {file_to_move} to {destination}")

            except shutil.SameFileError:
                # If source and destination are same
                print("Source and destination represents the same file.")
                logging.warning("Source and destination represents the same file.")

            except shutil.Error as e:
                print(f"Error moving the file: {e}")
                logging.error(f"Error moving the file: {e}")
                exit(1)


# In[48]:


def main():
    print("\n\nWelcome to the File Organizer!\n")
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='FileSorter - Organize Your Chaos')
    parser.add_argument('directory', type=str, help='The directory path you want to organize')
    args = parser.parse_args()

    # Access the directory argument
    selected_directory = args.directory
    directory_check(selected_directory)
    
    # Ask for backup
    backup = input("\nDo you want to create a Backup?\n Y \\ n  :  ")
    backup = backup.lower()
    
    if backup == "y":
        create_backup(selected_directory)
        
    logging.debug(f"backup finished succesfully")
    print("\n---------- BACKUP FINISHED ----------")
    
    print("---------- ORGANIZING FILES ----------\n")
    
    files = os.listdir(selected_directory)

    # Configure the logging
    logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

    # Create the nessesary folders and save the name of the existing ones
    # if there is not an images folder
    if not "images" in convert_list_to_lowercase(files):
        try:
            # create an images folder
            os.mkdir(selected_directory + "\\images")
            print("Created images folder")
            logging.debug(f"Created 'images' folder at: {os.path.join(selected_directory, 'images')}")
            # save the name of the folder
            image_folder = "images"
        except OSError as e:
            print(f"Error creating the 'images' folder: {e}")
            logging.error(f"Error creating the 'images' folder:: {e}")
    else: 
        # save the name of the existing folder as it is
        image_folder = files[convert_list_to_lowercase(files).index("images")]
        logging.debug(f"images folder already exist.")


    # if there is not a videos folder
    if not "videos" in convert_list_to_lowercase(files):
        try:
            # create a videos folder
            os.mkdir(selected_directory + "\\videos")
            print("Created videos folder")
            logging.debug(f"Created 'videos' folder at: {os.path.join(selected_directory, 'videos')}")
            # save the name of the folder
            video_folder = "videos"
        except OSError as e:
            print(f"Error creating the 'videos' folder: {e}")
            logging.error(f"Error creating the 'videos' folder: {e}")
    else:
        # save the name of the existing folder as it is
        video_folder = files[convert_list_to_lowercase(files).index("videos")]
        logging.debug(f"videos folder already exist.")

    # if there is not a music folder
    if not "music" in convert_list_to_lowercase(files):
        try:
            # create a music folder
            os.mkdir(selected_directory + "\\music")
            print("Created music folder")
            logging.debug(f"Created 'music' folder at: {os.path.join(selected_directory, 'music')}")
            # save the name of the folder
            music_folder = "music"
        except OSError as e:
            print(f"Error creating the 'music' folder: {e}")
            logging.error(f"Error creating the 'music' folder: {e}")
    else:
        # save the name of the existing folder as it is
        music_folder = files[convert_list_to_lowercase(files).index("music")]
        logging.debug(f"music folder already exist.")

    # if there is not a documents folder
    if not "documents" in convert_list_to_lowercase(files):
        try:
            # create a documents folder
            os.mkdir(selected_directory + "\\documents")
            print("Created documents folder")
            logging.debug(f"Created 'documents' folder at: {os.path.join(selected_directory, 'documents')}")
            # save the name of the folder
            documents_folder = "documents"
        except OSError as e:
            print(f"Error creating the 'documents' folder: {e}")
            logging.error(f"Error creating the 'documents' folder: {e}")
    else:
        # save the name of the existing folder as it is
        documents_folder = files[convert_list_to_lowercase(files).index("documents")]
        logging.debug(f"documents folder already exist.")


    # Counters
    images = 0
    videos = 0
    music = 0
    documents = 0


    # Read image extensions from the file
    image_extention = read_extensions_from_file("image extensions.txt")
    video_extention = read_extensions_from_file("video extensions.txt")
    music_extention = read_extensions_from_file("music extensions.txt")


    # Convert the lists to lowrcase
    image_extention = convert_list_to_lowercase(image_extention)
    video_extention = convert_list_to_lowercase(video_extention)
    music_extention = convert_list_to_lowercase(music_extention)


    # Move the files to folders
    for file in files:
        file_extension = get_file_extention(file)

        # if the file is not a folder
        if file_extension != "folder":
            # select the file   
            file_to_move = os.path.join(selected_directory, file)

            # if the the file has an image extention
            if file_extension in image_extention:
                images += 1
                # select the directory
                destination = os.path.join(selected_directory, image_folder)
                try:
                    # move the file to the specified directory
                    shutil.move(file_to_move, destination)
                    print(f"Moving {file_to_move} to {destination}")
                    logging.debug(f"Moving {file_to_move} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

            # if the the file has a video extention
            elif file_extension in video_extention:
                videos += 1
                # select the directory
                try:
                    # move the file to the specified directory
                    shutil.move(file_to_move, destination)
                    print(f"Moving {file_to_move} to {destination}")
                    logging.debug(f"Moving {file_to_move} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

            # if the the file has a music extention
            elif file_extension in music_extention:
                music += 1
                # select the directory
                destination = os.path.join(selected_directory, music_folder)
                try:
                    # move the file to the specified directory
                    shutil.move(file_to_move, destination)
                    print(f"Moving {file_to_move} to {destination}")
                    logging.debug(f"Moving {file_to_move} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

            # if the the file has a any other extention
            else:
                documents += 1
                # select the directory
                destination = os.path.join(selected_directory, documents_folder)
                try:
                    # move the file to the specified directory
                    shutil.move(file_to_move, destination)
                    print(f"Moving {file_to_move} to {destination}")
                    logging.debug(f"Moving {file_to_move} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

        # if the file is a folder
        else:
            pass


    number_of_files = images + videos + music + documents

    print("\n\n----------------------------")
    print(f"     {str(number_of_files)} files organized")
    print("----------------------------\n")
    logging.info(f"{str(number_of_files)} files organized")

    folders = {
        "documents": documents,
        "images": images,
        "music": music,
        "videos": videos,
    }

    # Sort the dictionary by its values in descending order
    sorted_folders = sorted(folders.items(), key=lambda x: x[1], reverse=True)

    print("Summary: ")
    for folder, count in sorted_folders:
        print(f"{count} {folder} has moved to " + os.path.join(selected_directory, f"{folder}"))
        logging.info(f"{count} {folder} has moved to " + os.path.join(selected_directory, f"{folder}"))

    print("\nOrganizing completed successfully! Your files are now organized.")
    logging.info("Organizing completed successfully! Your files are now organized.")


# In[49]:


logging.shutdown()


# In[50]:


if __name__ == "__main__":
    main()

