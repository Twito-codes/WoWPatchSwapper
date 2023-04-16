def change_realmlist(servers, profile, wow_folder):
    """
    Swaps realmlists based on value in Data.json

    :param servers: dict, Servers dictionary from Data.json
    :param profile: str, Key of the server in SERVERS
    :param wow_folder: str, Path to WoW folder
    """

    new_realmlist = servers[profile]["realmlist"]
    with open(wow_folder + "Data/enUS/realmlist.wtf", "w") as realmlist:
        realmlist.write(f"set realmlist {new_realmlist}")
