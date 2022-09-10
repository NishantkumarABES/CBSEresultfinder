#connection between python and internet
import pandas as pd
import matplotlib.pyplot as pl
import statistics
a=int(input("Enter your start roll number:"))
c=int(input("Enter your end roll number:"))
d=(c+1)-a
print("Number of students:",d)
b=60274
list=[]
list1=[]
while a<=c:
    from selenium import webdriver
    driver=webdriver.Chrome(r"D:\User Data\Desktop\nishant\selenium\chromedriver.exe")
    driver.get(r"https://cbseresults.nic.in/class12/Class12th21.htm")
    enter_roll_no=driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[1]/td[2]/input")
    enter_school_no=driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[2]/td[2]/input")
    enter_roll_no.send_keys(a)
    enter_school_no.send_keys(b)
    summit_button=driver.find_element_by_xpath("/html/body/table[3]/tbody/tr/td/font/center[2]/form/div[1]/center/table/tbody/tr[3]/td/input[1]")
    summit_button.click()
    name=driver.find_element_by_xpath("/html/body/div/table[1]/tbody/tr[2]/td[2]/font/b").text
    f=name
    list1.append(f)
    eng=driver.find_element_by_xpath("/html/body/div/div/center/table/tbody/tr[2]/td[5]/font").text
    phy=driver.find_element_by_xpath("/html/body/div/div/center/table/tbody/tr[3]/td[5]/font").text
    chem=driver.find_element_by_xpath("/html/body/div/div/center/table/tbody/tr[4]/td[5]/font").text
    math=driver.find_element_by_xpath("/html/body/div/div/center/table/tbody/tr[5]/td[5]/font").text
    ip=driver.find_element_by_xpath("/html/body/div/div/center/table/tbody/tr[6]/td[5]/font").text
    per=(int(eng)+int(phy)+int(chem)+int(math)+int(ip))/5
    e=per
    list.append(e)
    a=a+1
    driver.close()
u={"Name":list1,"Perctange":list}
g=pd.DataFrame(u)
print(g)
print("___________________________________________________________")
q=max(list)
i1=list.index(q)
n1=list1[i1]
list.remove(q)
w=max(list)
list.insert(i1,q)
i2=list.index(w)
n2=list1[i2]
list.remove(w)
list.remove(q)
t=max(list)
list.insert(i1,q)
list.insert(i2,w)
i3=list.index(t)
n3=list1[i3]
mi=min(list)
i4=list.index(mi)
n4=list1[i4]
print("rank-1",n1,q)
print("rank-2",n2,w)
print("rank-3",n3,t)
print("___________________________________________________________")
print("lowest percentage:",n4,mi)
print("___________________________________________________________")
stat=statistics.mean(list)
print("Average percentage of class:",stat)
list3=[]
for g in range(0,d):
    if list[g]>90:
        list3.append(g)
    else:
        print()
print("___________________________________________________________")
print("Number of student score above 90:",len(list3))
        
    



















