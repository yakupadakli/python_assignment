# -*- coding: utf-8 -*-


file = open("test.log", "r")
sayi = file.readlines().__len__()
file.close()
file = open("test.log", "r")
links = []
time_dict = {}
time_list = []
count_dict = {}
x = 0
for i in range(sayi):
    yazi = file.readline()

    time = yazi[yazi.find("~ ")+2:yazi.find('\n')]
    time_list.append(time)
    a = yazi.find('"')
    temp = yazi[a:]
    b = temp.find(" HTTP")

    if "GET" in yazi:
        link = yazi[a + 5:a + b]
    elif "POST" in yazi:
        link = yazi[a + 6:a + b]
    elif "HEAD" in yazi:
        link = yazi[a + 6:a + b]
    elif "PUT" in yazi:
        link = yazi[a + 5:a + b]
    elif "DELETE" in yazi:
        link = yazi[a + 8:a + b]
    elif "OPTIONS" in yazi:
        link = yazi[a + 9:a + b]

    links.append(link)
    time_dict.update({time: link})

    if link in count_dict:
        count_dict[link] += 1
    else:
        count_dict.update({link: 1})

#
# temp_links = links
# print temp_links.__len__()
# for i in range(diffList.__len__()):
#     if diffList[i] in links:
#         temp_links.remove(diffList[i])
#
#
# print temp_links.__len__()

# for i in range(diffList.__len__()):
#     counts = links.count(diffList[i])
#     count_dict.update({diffList[i]: counts})
#
# print count_dict.__len__()
# print count_dict


print "Most requested urls : " + str(max(count_dict.keys(), key=count_dict.get))
print "Most requested urls count : " + str(count_dict[max(count_dict.keys(), key=count_dict.get)])

print "Most time consuming urls : " + str(time_dict[max(time_dict)])
print "Most time consuming urls time : " + str(max(time_dict))
file.close()
