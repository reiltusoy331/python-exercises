filetypes = ['doc', 'txt', 'png', 'jpeg', 'gif', 'csv', 'xml']

filename = input('Insert file with extension: ').split('.')
if len(filename) >= 2:
    extension = filename[-1].lower()
    if extension in filetypes:
        print('The file extension is in \'' + extension + '\' form.')
    else:
        print('The file extension \'' + extension + '\' doesn\'t exist')
else:
    print('File doesn\'t have an extension')
