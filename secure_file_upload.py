def secure_login(username, password):
    username_ = "Mike"
    password_ = 123
    if username == username_:
        if password == password_:
            return True
    return False
    # Errors 001, 002, 006

def uploader(type_in):
    #type_in = input("file or image? : ")
    #file_name = input("Enter the name of the file you are uploading: ") 
    if type_in == "file":
        return True
    elif type_in == "image":
        return True
    else:
        return False
    # Error 008

def checker(file_name):
    if file_name.endswith('.txt'):
        print('valid')
        return True
    if file_name.endswith('.test'):
        print('valid')
        return True
    else:
        print( "Error related to uploader")
        return False
    # Error 001


