import shutil


def remove_old_patches(servers, profile, wow_folder):
    """
    Moves patches of last server to Unused_patches folder.

    :param servers: dict, Servers dictionary in Data.json
    :param profile: str, Key of server in SERVERS
    :param wow_folder: str, Path to WoW folder
    """
    for patch in servers[profile]["patches"]:
        src = wow_folder + "Data/" + patch
        dst = wow_folder + "Data/Unused_patches/" + profile + '/' + patch
        shutil.move(src, dst)


def move_current_patches(servers, profile, wow_folder):
    """
    Moves patches of the server you are trying to connect to WoW's Data Folder

    :param servers: dict, Servers dictionary in Data.json
    :param profile: str, Key of server in SERVERS
    :param wow_folder: str, Path to WoW folder
    """
    for patch in servers[profile]["patches"]:
        src = wow_folder + "Data/Unused_patches/" + profile + '/' + patch
        dst = wow_folder + "Data/" + patch
        shutil.move(src, dst)
