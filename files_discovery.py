def get_files(folderpath)-> List[str]:
    """Discover all files from folderpath and return a list of all filepaths.
    Parameters
    ----------
    folderpath : str
        root dir of files
    Returns
    -------
    List
        List of files in path
    """
    all_files = []
    for root, dirs, files in os.walk(folderpath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    return all_files
