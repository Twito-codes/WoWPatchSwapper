import shutil


def next_profile(profile, profiles):
    """
    Swaps profiles in the script.

    :param profile: string, Current profile
    :param profiles: list, list of profiles
    :return: string, next profile in list
    """
    profile_index = profiles.index(profile)
    try:
        current_profile = profiles[profile_index + 1]
    except IndexError:
        current_profile = profiles[0]
    return current_profile


def delete_cache(wow_folder):
    try:
        shutil.rmtree(wow_folder + 'Cache')
    except FileNotFoundError:
        pass
