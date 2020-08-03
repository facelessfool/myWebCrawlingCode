import pywikibot

site = pywikibot.Site("en", "wikipedia")
page = pywikibot.Page(site, "Main_Page")
revs = page.revisions()


item_list = list(revs)

item_count = len(item_list)
print("Number of entries:", item_count)

print(" ")
print(" ")
print("first entry: ", item_list[0])

# d_t = str(item_list[29].timestamp)
# print("d_t: ", d_t)
# d_t_list = d_t.split("T")
# date1 = d_t_list[0]
# time1 = d_t_list[1]
# slice_object = slice(5)

# time1 = time1[slice_object]

# print("date: ", date1)
# print("time: ", time1)

# print("timestamp: ", )

print(" ")
print(" ")
print("2nd entry: ", item_list[1])


print(" ")
print(" ")
print("3rd entry: ", item_list[2])

print(" ")
print(" ")
print("4th entry: ", item_list[3])


# print("Entry number 20,731 is:", item_list[20730])
