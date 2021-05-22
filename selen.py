from selenium import webdriver

# Sadece bu kismin alti degistirilecek
list1 = "https://open.spotify.com/playlist/60Xe5cJDpcbiHbWwsayOsj?si=3b247bf0ece24ede"
list2 = "https://open.spotify.com/playlist/4rEP2SYmsoGWRvXIc7W6qd?si=45ca9bff1d1c4794"
# Sadece bu kismin ustu degistirilecek

def Getting_account1(acclist1):
  driver = webdriver.Chrome(r"C:\chromedriver")
 
  driver.get(acclist1)
  driver.implicitly_wait(2)
  driver.maximize_window()
  sarki_isim = driver.find_elements_by_class_name('_8ea0b892e971e6b90a252247c160b4f4-scss')
  i = 0
  sarkilar = " "
  yazarlar = " "
  sarkilist = []
  yazarlist = []

  for x in sarki_isim:
    sarkilist.append(sarki_isim[i].text.split("\n")[0])
    i += 1
  return sarkilist



def Getting_account2(acclist2):
  driver = webdriver.Chrome(r"C:\chromedriver")
  driver.get(acclist2)
  driver.implicitly_wait(2)
  driver.maximize_window()
  sarki_isim = driver.find_elements_by_class_name('_8ea0b892e971e6b90a252247c160b4f4-scss')
  i = 0

  sarkilar = " "
  yazarlar = " "
  sarkilist = []
  yazarlist = []

  for x in sarki_isim:
    sarkilist.append(sarki_isim[i].text.split("\n")[0])
    i += 1
  return sarkilist

ayni_sarkilar = []

ready_list1 = Getting_account1(list1)
ready_list2 = Getting_account2(list2)

enkucuk = ""
enbuyuk = ""

if len(ready_list1) > len(ready_list2):
  enkucuk = ready_list2
  enbuyuk = ready_list1
else:
  enkucuk = ready_list1
  enbuyuk = ready_list2

for i in enbuyuk:
  if i in enkucuk:
    ayni_sarkilar.append(i)
  else:
    next
print(ayni_sarkilar)
    
