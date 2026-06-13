# Linux Hands-On Practice

## Task 1 - Check Current Directory

pwd

Result:
Displayed the current working directory.

---

## Task 2 - List Files and Directories

ls

Result:
Displayed all files and folders in the current directory.

---

## Task 3 - List Detailed Information

ls -l

Result:
Displayed permissions, owner, size, and modification date.

---

## Task 4 - List Hidden Files

ls -a

Result:
Displayed hidden files and directories.

---

## Task 5 - Create Directory

mkdir devops-project

Result:
Created a new directory named devops-project.

---

## Task 6 - Change Directory

cd devops-project

Result:
Moved into the devops-project directory.

---

## Task 7 - Create Empty File

touch notes.txt

Result:
Created an empty file.

---

## Task 8 - View File Content

cat notes.txt

Result:
Displayed file contents.

---

## Task 9 - Copy File

cp notes.txt backup.txt

Result:
Created a copy of notes.txt.

---

## Task 10 - Rename File

mv backup.txt final.txt

Result:
Renamed backup.txt to final.txt.

---

## Task 11 - Delete File

rm final.txt

Result:
Deleted the file successfully.

---

## Task 12 - Display Current User

whoami

Result:
Displayed the currently logged-in user.

---

## Task 13 - Display Linux Information

uname -a

Result:
Displayed Linux kernel and system information.

---

## Task 14 - Display Command History

history

Result:
Displayed previously executed commands.

---

## Task 15 - Search Text

grep "ERROR" application.log

Result:
Displayed lines containing the word ERROR.

---

## Task 16 - Case-Insensitive Search

grep -i "linux" notes.txt

Result:
Displayed all matching words regardless of case.

---

## Task 17 - View First Lines

head notes.txt

Result:
Displayed the first 10 lines.

---

## Task 18 - View Last Lines

tail notes.txt

Result:
Displayed the last 10 lines.

---

## Task 19 - Check Running Processes

ps

Result:
Displayed active processes.

---

## Task 20 - Monitor Processes

top

Result:
Displayed real-time system resource usage.

---

## Task 21 - Kill Process

kill 1234

Result:
Terminated process ID 1234.

---

## Task 22 - Check Disk Usage

df -h

Result:
Displayed disk usage in human-readable format.

---

## Task 23 - Change File Permissions

chmod 755 script.sh

Result:
Made the script executable.

---

## Task 24 - Download File

wget https://example.com/file.zip

Result:
Downloaded a file from the internet.

---

## Task 25 - Connect to Remote Server

ssh user@server-ip

Result:
Connected securely to a remote Linux server.

---

## Task 26 - Create Archive

tar -cvf backup.tar project/

Result:
Created a tar archive.

---

## Task 27 - Extract Archive

tar -xvf backup.tar

Result:
Extracted archived files.

---

## Task 28 - Create Zip File

zip project.zip notes.txt

Result:
Compressed file into zip format.

---

## Task 29 - Extract Zip File

unzip project.zip

Result:
Extracted zip contents.

---

## Task 30 - Create Alias

alias ll='ls -la'

Result:
Created shortcut command for detailed listing.

---

## Task 31 - Find Command Location

whereis grep

Result:
Displayed binary and manual page locations.

---

## Task 32 - Command Description

whatis grep

Result:
Displayed short description of grep command.

---

## Task 33 - Display Network Information

ifconfig

Result:
Displayed network interface details.

---

## Task 34 - Use Super User Privileges

sudo apt update

Result:
Executed command with administrative privileges.
