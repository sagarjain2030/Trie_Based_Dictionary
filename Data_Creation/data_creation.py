
def generate_file_paths():
    '''
    Summary:
        Returns list of file paths for all alphabets.

    Parameters:
        None

    Returns:
        List of file paths generated for all alphabets
    
    Description:
        We want to store words and their meaning in file depending upon words starting letter. For this purpose, we need to know each individual file path for storing these data.
    '''

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    ls_file_paths = []
    file_name_prefix = "list_Dictionary/"
    file_name_suffix = "_words.txt\n"
    for elem in alphabets:
        ls_file_paths.append(file_name_prefix + elem + file_name_suffix)
    return ls_file_paths

def generate_file_path_dictionary():
    '''
    Summary:
        Generate all alphabet file paths and write in a dictionary txt file
    
    Parameters:
        None
    
    Return:
        None
    '''
    ls_file_paths = generate_file_paths()
    with open("dictionary_list.txt", 'w') as f:
        for elem in ls_file_paths:
            f.write(elem)

def main():
    '''
    Summary: 
        Main fnction to call methods for data creation
    
    Parameters: 
        None

    Returns:
        None
    '''
    generate_file_path_dictionary()
    #Generate_Urls_Dictionary()
    #Get_data_from_url()

if __name__=='__main__':
    main()