def secure_login():
    return "Login worked or didnt"

def uploader():
    print("file or image? : ")
    file_name = input("Enter the name of the file you are uploading: ")

def checker(file_name):
    if file_name.endswith('.txt'):
        print('valid')
    if file_name.endswith('.test'):
        print('valid')
    else:
        return "Error related to uploader"

