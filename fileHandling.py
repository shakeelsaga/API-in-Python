# with open("sample.txt", "w") as f:
#     f.write("This is line 1.\n")
#     f.write("This is line 2.\n")
#     f.write("This is line 3.\n")
#     f.write("This is line 4.\n")

# with open("sample.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("sample.txt", "a") as f:
#     for i in range(21, 31):
#         f.write(f"This is line {i}.\n")

# with open("sample.txt", "r") as f:
#     f.seek(21)
#     print(f.read())

# try:
#     file = open("sample.txt", "x")
# except FileExistsError:
#     print("File already exists. Please choose a different name or delete the existing file.")

# import requests

# # r = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Sunflower_from_Silesia2.jpg/1280px-Sunflower_from_Silesia2.jpg")
# # with open("image.jpg", "wb") as f:
# #     f.write(r.content)

#Q1:
# with open("text.txt", "w") as f:
#     f.write("konichiwa\n")
#     f.write("Please be carfull with the file handling\n")

#Q2:
# def find_word_occurence(filename, word):
#     i = 1
#     with open(filename, "r") as f:
#         for line in f:
#             if word in line:
#                 return i
#             i = i + 1
#     return -1

# word = "the"
# line = find_word_occurence("text.txt", word)

# if line != -1:
#     print(f"The word '{word}' was found in the line {line}")
# else:
#     print("Word not Found")

#Q3
# with open("numbers.txt", "r") as f:
#     data = f.read()
#     length = len(data)
#     count = 0
#     num = ""
#     for i in range(length):
#         if data[i] == ',':
#             print(int(num))
#             if int(num) % 2 == 0:
#                 count += 1
#             num = ""
#         else:
#             num += data[i]

#     print(int(num))
#     if int(num) % 2 == 0:
#         count += 1
        
#     print(count)