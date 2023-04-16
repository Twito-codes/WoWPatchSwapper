#   Requirements
Python 3

#   Setup
1. Go to WoW's Data folder and create Unused_patches folder.
2. Inside Unused_patches create folder for every profile you'll use. The name of the folder must be the same as profile name.
3. Inside scripts Data/Data.json fill in current profile and all profiles.
- PROFILE is a string
- PROFILES contains all profiles for PROFILE
- WOW_FOLDER is a string containing a path to your WoW directory. Must end with '/'!
- SERVERS has a key for every profile, its value is dict
- realmlist only contains the ip adress of server, no need for 'set realmlist ' string
- patches only requiere file names, for example 'patch-5.mpq'
