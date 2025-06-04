# Harvard exercise number 3

'''
prompt user for a file name with extension and return the type of file and extension
ex: happy.png = image/PNG
'''

# User Prompt

f = input("File Name: ")

# Sort file types

f = f.lower()
ft = f[-4:]

# IMAGES
if ft == ".png":
    print("Image/png")
elif ft == ".jpg":
    print("Image/jpeg")
elif ft == ".gif":
    print("Image/gif")
elif ft == ".zip":
    print("Application/zip")
elif ft == ".pdf":
    print("Application/pdf")
elif ft == ".txt":
    print("Text/plain")
else:
    print("application/octet-stream")

