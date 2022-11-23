'''
Summary : Creatinng Data for Trie Dictionary
'''

def generate_file_paths():
    '''
    Summary:
        Returns list of file paths for all alphabets.

    Parameters:
        None

    Returns:
        List of file paths generated for all alphabets

    Description:
        We want to store words and their meaning in file depending upon words starting letter.
        For this purpose, we need to know each individual file path for storing these data.
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
    with open("dictionary_list.txt", 'w' , encoding="utf-8") as file_open:
        for elem in ls_file_paths:
            file_open.write(elem)

def get_generated_urls():
    '''
    Summary:
        Generate url for each alphabet

    Parameters:
        None

    Return:
        List of Generated Urls for each alphabet
    '''
    list_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    url_list = []
    url_first_part = "https://www.mso.anu.edu.au/~ralph/OPTED/v003/wb1913_"
    url_last_part = ".html"
    for elem in list_alphabet:
        url_list.append(url_first_part + elem + url_last_part)
    return url_list

def generate_urls_dictionary():
    '''
    Summary:
        Write all urls into dictionary_urls file

    Parameter:
        None

    Return:
        None
    '''

    url_list = get_generated_urls()
    with open("dictionary_urls.txt" , 'w' , encoding="utf-8") as file_open:
        for elem in url_list:
            file_open.write(elem + "\n")

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
    generate_urls_dictionary()
    #Get_data_from_url()

if __name__=='__main__':
    main()
