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
    fileName = os.path.splitext(name)[1]
    if fileName == '':
        return "folder"
    else:
        return fileName


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


# In[47]:


def print_colored_text(color, text):
    color_codes = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
    }

    if color.lower() in color_codes:
        color_code = color_codes[color.lower()]
        return(f"\033[{color_code}m{text}\033[0m")
    else:
        return(text)


# In[48]:


def main():
    print("\n\nWelcome to the File Organizer!\n")
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='FileSorter - Organize Your Chaos')
    parser.add_argument('directory', type=str, help='The directory path you want to organize')
    args = parser.parse_args()

    # Access the directory argument
    selectedDirectory = args.directory
    directory_check(selectedDirectory)
    
    print("---------- Organizing files ----------\n")
    
    files = os.listdir(selectedDirectory)

    # Configure the logging
    logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

    # Create the nessesary folders and save the name of the existing ones
    # if there is not an images folder
    if not "images" in convert_list_to_lowercase(files):
        try:
            # create an images folder
            os.mkdir(selectedDirectory + "\\images")
            print("Created images folder")
            logging.debug(f"Created 'images' folder at: {os.path.join(selectedDirectory, 'images')}")
            # save the name of the folder
            imageFolder = "images"
        except OSError as e:
            print(f"Error creating the 'images' folder: {e}")
            logging.error(f"Error creating the 'images' folder:: {e}")
    else: 
        # save the name of the existing folder as it is
        imageFolder = files[convert_list_to_lowercase(files).index("images")]
        logging.debug(f"images folder already exist.")


    # if there is not a videos folder
    if not "videos" in convert_list_to_lowercase(files):
        try:
            # create a videos folder
            os.mkdir(selectedDirectory + "\\videos")
            print("Created videos folder")
            logging.debug(f"Created 'videos' folder at: {os.path.join(selectedDirectory, 'videos')}")
            # save the name of the folder
            videoFolder = "videos"
        except OSError as e:
            print(f"Error creating the 'videos' folder: {e}")
            logging.error(f"Error creating the 'videos' folder: {e}")
    else:
        # save the name of the existing folder as it is
        videoFolder = files[convert_list_to_lowercase(files).index("videos")]
        logging.debug(f"videos folder already exist.")

    # if there is not a music folder
    if not "music" in convert_list_to_lowercase(files):
        try:
            # create a music folder
            os.mkdir(selectedDirectory + "\\music")
            print("Created music folder")
            logging.debug(f"Created 'music' folder at: {os.path.join(selectedDirectory, 'music')}")
            # save the name of the folder
            musicFolder = "music"
        except OSError as e:
            print(f"Error creating the 'music' folder: {e}")
            logging.error(f"Error creating the 'music' folder: {e}")
    else:
        # save the name of the existing folder as it is
        musicFolder = files[convert_list_to_lowercase(files).index("music")]
        logging.debug(f"music folder already exist.")

    # if there is not a documents folder
    if not "documents" in convert_list_to_lowercase(files):
        try:
            # create a documents folder
            os.mkdir(selectedDirectory + "\\documents")
            print("Created documents folder")
            logging.debug(f"Created 'documents' folder at: {os.path.join(selectedDirectory, 'documents')}")
            # save the name of the folder
            documentsFolder = "documents"
        except OSError as e:
            print(f"Error creating the 'documents' folder: {e}")
            logging.error(f"Error creating the 'documents' folder: {e}")
    else:
        # save the name of the existing folder as it is
        documentsFolder = files[convert_list_to_lowercase(files).index("documents")]
        logging.debug(f"documents folder already exist.")


    # Counters
    images = 0
    videos = 0
    music = 0
    documents = 0


    # Read image extensions from the file
    imageExtention = read_extensions_from_file("image extensions.txt")
    videoExtention = read_extensions_from_file("video extensions.txt")
    musicExtention = read_extensions_from_file("music extensions.txt")


    # Convert the lists to lowrcase
    imageExtention = convert_list_to_lowercase(imageExtention)
    videoExtention = convert_list_to_lowercase(videoExtention)
    musicExtention = convert_list_to_lowercase(musicExtention)


    # Move the files to folders
    for file in files:
        fileExtension = get_file_extention(file)

        # if the file is not a folder
        if fileExtension != "folder":
            # select the file   
            fileToMove = os.path.join(selectedDirectory, file)

            # if the the file has an image extention
            if fileExtension in imageExtention:
                images += 1
                # select the directory
                destination = os.path.join(selectedDirectory, imageFolder)
                try:
                    # move the file to the specified directory
                    shutil.move(fileToMove, destination)
                    print(f"Moving {fileToMove} to {destination}")
                    logging.debug(f"Moving {fileToMove} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

            # if the the file has a video extention
            elif fileExtension in videoExtention:
                videos += 1
                # select the directory
                try:
                    # move the file to the specified directory
                    shutil.move(fileToMove, destination)
                    print(f"Moving {fileToMove} to {destination}")
                    logging.debug(f"Moving {fileToMove} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

            # if the the file has a music extention
            elif fileExtension in musicExtention:
                music += 1
                # select the directory
                destination = os.path.join(selectedDirectory, musicFolder)
                try:
                    # move the file to the specified directory
                    shutil.move(fileToMove, destination)
                    print(f"Moving {fileToMove} to {destination}")
                    logging.debug(f"Moving {fileToMove} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

            # if the the file has a any other extention
            else:
                documents += 1
                # select the directory
                destination = os.path.join(selectedDirectory, documentsFolder)
                try:
                    # move the file to the specified directory
                    shutil.move(fileToMove, destination)
                    print(f"Moving {fileToMove} to {destination}")
                    logging.debug(f"Moving {fileToMove} to {destination}")
                except shutil.Error as e:
                    print(f"Error moving the file: {e}")
                    logging.error(f"Error moving the file: {e}")

        # if the file is a folder
        else:
            pass


    numberOfFiles = images + videos + music + documents

    print("\n\n----------------------------")
    print(f"     {str(numberOfFiles)} files organized")
    print("----------------------------\n")
    logging.info(f"{str(numberOfFiles)} files organized")

    folders = {
        "documents": documents,
        "images": images,
        "music": music,
        "videos": videos,
    }

    # Sort the dictionary by its values in descending order
    sortedFolders = sorted(folders.items(), key=lambda x: x[1], reverse=True)

    print("Summary: ")
    for folder, count in sortedFolders:
        print(f"{count} {folder} has moved to " + os.path.join(selectedDirectory, f"{folder}"))
        logging.info(f"{count} {folder} has moved to " + os.path.join(selectedDirectory, f"{folder}"))

    print("\nOrganizing completed successfully! Your files are now organized.")
    logging.info("Organizing completed successfully! Your files are now organized.")


# In[49]:


logging.shutdown()


# In[50]:


if __name__ == "__main__":
    main()

