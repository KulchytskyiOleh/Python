from tkinter import*
import requests
from bs4 import BeautifulSoup
from datetime import date

root = Tk()
root.title('Вільні аудиторії')
root.geometry('1000x445')

sqdate = StringVar()

sqdate_label = Label(text="Введіть дату у форматі 11.12.18 :  ")
 
sqdate_label.grid(row=0, column=0, sticky="w")
 
sqdate_entry = Entry(textvariable=sqdate, width=24)
 
sqdate_entry.grid(row=1, column=0, padx=5, pady=5)

text=Text(width=100, height=20)
text.grid(row=4,column=2)

dict_room = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set()}

dict_room_2 = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set()}

room = {
       '207', '229', '230', '231', '232',  '234',
       '301', '303', '305', '306', '307', '307a', '307б', '309', '310',
       '313', '316', '318',  '320', '322', '324', '325',
       '402', '403', '404',  
        }

dict_room_free = {1: room, 2: room, 3: room, 4: room, 5: room, 6: room, 7: room}

groups = {'ПМ-11(к)','ПМ-12(к)', 'СМ-6', 'ІСТ-1', 'СО(М)(з)11', 'ПМ-2', 'СО(М)-2', 'СО(І)-5м',
          'ІНФ-42', 'ПМк-41', 'М(ас)-11', 'ПМ-4', 'КН-21', 'МАТ-32', 'І(з)-41', 'МАТ-41',
          'КН(з)-11', 'ІНФ-41', 'См-5', 'ПМ к- 31', 'ПМ к- 31','ПМ к- 41',  'СОМ-5м', 'СО(І)(з)11', 'С-3',
          'ПМ-3', 'М(ас)-21', 'С-4', 'ПМк-21', 'СО(І)-1', 'СОМ(І)(з)6', 'КН-11', 'КН-52м',
          'СОМ(М)(з)6', 'ІПЗ-1', 'ІПЗ-2', 'ІПЗ-3', 'СО(М)-1', 'Ст-2', 'ПМ-1', 'М(докт)-1', 'СО(І)-5м.', 'ПМ-51',
          'МАТ-31', 'М(докт)-2', 'ПМ-52м', 'М-52м', 'СО(І)-2', 'СО(І)(з)21', 'М-2', 'СОМ(М)(з)-',
          'ПІ-3', 'І(з)-31', 'МАТ-42', 'КН(з)-21', 'ІНФ-32', 'ІС(з)-11', 'СО(М)(з)21', 'М-51',
          'ПМ-12(к)', 'СОМ(І)(з)5', 'Ст-1', 'ПМк-22', 'КН-51м', 'КН-22', 'М-1', 'ІНФ-31',
          'ІСТ-2', 'СО(М)-3', 'СО(І)-3',
          'КН-1', 'КН-2', 'КН-31', 'КН-32', 'КНМ-1', 'КНМ-2', 
	  'ІСТ-1', 'ІСТ-2',
	  'ПММ -1', 'ПММ-1', 'ПММ-2',
	  'М -2', 'М - 41', 'М - 42',
          'ММа-1', 'ММк-1', 'СОМ(М)-1', 'СОМ(І)-1',
          'СМ -2', 'СОМ(М)-2', 'СОМ (І)-2',
          'ПІ-4', 'І-4',  'СО(I)-1', 'М-3',
          'С-3',
          'ПМ(к)-11', 'ПМ(к)-12', 'ПМ-21(к)', 'ПМ-22(к)', 'ПМ к- 31', 'ПМ к- 32', 'ПМ к- 41',
          'І-41'
          }
def deleteText():
    text.delete(1.0, END)

def parser():
    sdate=sqdate.get()
    if sdate == '':
          today = date.today()  
          sdate = today.strftime("%d.%m.%y")
          edate = today.strftime("%d.%m.%y")
    else:
          edate = sdate

    group = 'ПММ-2'

    url = "http://asu.pnu.edu.ua/cgi-bin/timetable.cgi"
    headers = {'Content-Type': 'text/html; charset=windows-1251'}

    data = {'group': group.encode('cp1251'), 'sdate': sdate, 'edate': edate}

    r = requests.post(url, headers=headers, data = data )

    r.encoding = 'cp1251'
          
    flag = 0

    for group in groups:
          r = requests.post(url, headers=headers,
                            data = {'group': group.encode('cp1251'), 'sdate': sdate,
                                                          'edate': edate, 'n': '700'})
          r.encoding = 'cp1251'

          soup = BeautifulSoup(r.text, "html.parser")
          rows = soup.find_all('tr') 
                    
          if rows:
                for row in rows:
                      cols = row.find_all('td')
                      if cols[2].text != '':
                            index = int(rows.index(row))
                            number_line = index + 1

                            if len(cols[2].text.split()):
                                  elem_room = cols[2].text.split()[0] 
                                  elem_room_2 = elem_room +'('+ cols[2].text.split()[1]+')'
                            else:
                                  elem_room = ''
        
                            if elem_room != '':                                                     
                                  dict_room[number_line].add(elem_room)
                                  dict_room_2[number_line].add(elem_room_2)
       
    for k in reversed(range(1,7)):
        f = dict_room_free[k].difference(dict_room[k])
        text.insert(1.0,("|{}пара|\nвільні аудиторії: {}\n".format(k, ', '.join(sorted(f)))))
   
button = Button(text="Показати вільні аудиторії", command=parser)
button.grid(row=2,column=0)
buttonclear = Button(text="Очистити", command=deleteText, width=20)
buttonclear.grid(row=3,column=0,padx=5, pady=5)

root.mainloop()
