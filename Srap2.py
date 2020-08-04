import pywikibot
import pandas as pd
i=1
site = pywikibot.Site("en", "wikipedia")
titles_list=[  "Beowulf","Quran","Rosetta_Stone","Divine_Comedy","Mahabharata","Iliad","Ramayana",
      "The_Art_of_War","Epic_of_Gilgamesh","Vedas","The_Canterbury_Tales","One_Thousand_and_One_Nights",
       "Talmud","Code_of_Hammurabi","I_Ching","Oedipus_Rex",
      "Aeneid","Book_of_the_Dead","Rigveda","Domesday_Book","Tao_Te_Ching","Upanishads","Cupid_and_Psyche",
       "Lysistrata","Titanomachy",
      "The_Decameron"]
for title_item in titles_list:
    title1=title_item
    path2="normal_"+title1+".csv"
    
    # path2="normal_WikipediaFeatured_content.csv"

    page=pywikibot.Page(site, title1)
    
    revs=page.revisions()
    itemsList=list(revs)
    #empty lists to store values
    date_list=[]
    time_list=[]
    user_list=[]
    minor_list=[]
    final_list=[]

    for entry in reversed(itemsList):
        d_t = str(entry.timestamp)
        d_t_list = d_t.split("T")
        date1 = d_t_list[0]
        time1 = d_t_list[1]
        slice_object = slice(5)

        time1 = time1[slice_object]

    #     print("data: ", date1)
    #     print("time: ",time1)
        date_list.append(date1)
        time_list.append(time1)
        user1=entry.user
        if (user1==""):
            user1="username empty"
        user_list.append(user1)


        if (entry.minor):
            m=1
        else:
            m=0
        minor_list.append(m)


    for date_item, time_item, user_item, m_item in zip(date_list,time_list,user_list,minor_list):
        final_list.append({'Date':date_item, 'Time':time_item,'user1':user_item,'user2':user_item, 'm':m_item})
    df=pd.DataFrame(final_list)

    path1='C:/Users/Kajal Chingsubam/Desktop/'
    df.to_csv(


            path1+path2,


        index=False, encoding="utf-8")


    print(i)
    i+=1