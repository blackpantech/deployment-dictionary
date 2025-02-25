# Deployment Dictionary

## Description

"Deployment Dictionary" is a deployment helper. This script aims at replacing flagged variables in text files in a
specified directory with a manually written dictionary. In the dictionary file, you associate a variable with a
literal value.

## Before using

### Setting up the environment
You need to define 3 environment variables:
- 'DICO': path to the dictionary file (for example: "/home/<USER>/dico/<USER>.dico")
- 'CONF': path to the directory to execute the script on (for example: "/home/<USER>/conf")
- 'CONFIG_FILE_EXTENSION': file type to execute the script on (for example: "properties")

### Making a dictionary file
In your dictionary file, you can declare variables to look for and replace in your configuration files. These variables
are declared with name, an equal sign ("=") and literal value. Make sure every variable is unique in the file.

For example:

entry1.value=entry1_value
entry1.key=entry1_key
entry2.value="entry2_value"
entry3=3

### Configuration files to modify
In your specified 'CONF' directory, you should have files of the same type set up in 'CONFIG_FILE_EXTENSION'.
The script will ignore other file types.

To declare a variable in a configuration file, flag it with its name surrounded by curly brackets.

For example:

{{entry1.value}}

## User manual
To launch the script, simply type ``python3 ./src/main.py`` from the project root. At the end of the script, you can see
that the variables flagged in configuration files with a dictionary entry in the dictionary file were replaced with
their appropriate values.

## Features backlog
- [ ] Get dictionary file path from directory only. The file will need to be named '<USER>.dico', where <USER> is the Linux username
- [ ] Missing variables in dictionary:
  - [X] Finding missing variable entries in target files
  - [ ] Prompting user to manually replace missing variables
  - [ ] Adding missing variables to dictionary file
- [ ] Handle default values if no entry is found in the dictionary (e.g: {{entry1.value:default-value}})
