def get_files(filepath):
    """Discover all files from filepath and return
    a list of all filepaths.
    Parameters
    ----------
    filepath : str
        root dir of files
    Returns
    -------
    List
        List of files paths
    """
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    return all_files
