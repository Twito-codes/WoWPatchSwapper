from Functions.ChangeRealmlist.Realmlist import change_realmlist
from Functions.Logging.logger import swapper_logger
from Functions.MovePatches.MovePatches import move_current_patches, remove_old_patches
from Functions.Utils.utils import next_profile, delete_cache
from Functions.Utils.jsonUtils import load_data, update_data


def main():
    data = load_data()
    swapper_logger.info("--------------------------NEW RUN-------------------------")
    remove_old_patches(servers=data["SERVERS"], profile=data["PROFILE"], wow_folder=data["WOW_FOLDER"])
    data["PROFILE"] = next_profile(profile=data["PROFILE"], profiles=data["PROFILES"])
    move_current_patches(servers=data["SERVERS"], profile=data["PROFILE"], wow_folder=data["WOW_FOLDER"])
    change_realmlist(servers=data["SERVERS"], profile=data["PROFILE"], wow_folder=data["WOW_FOLDER"])
    delete_cache(data["WOW_FOLDER"])
    update_data(data)

    print(f"Loaded profile {data['PROFILE']}.")


if __name__ == "__main__":
    main()
    input("Press any key to exit…")
