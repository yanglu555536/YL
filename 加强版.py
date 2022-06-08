import os
import glob
import datetime,time

#for i in range(6,9):

now=time.strftime("%Y-%m-%d %H:%M:%S")
print(now)


a=input("请输入一个时段哦(例：05_06_19)：")






#1A
try:
      target_path=os.path.join(r"\\10.32.12.22\PVCTData\ClassA\2022_"+a)
      all_content= os.listdir(target_path)
      target_path2=os.path.join(r"\\10.32.12.22\PVCTData\ClassB\2022_"+a)
      all_content2= os.listdir(target_path2)
      
      
      print(r"1A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content))),(int(len(all_content2))-1))
except:
      print(r"1A 2022_"+str(a)+" 时段A B级片数量为 0  0")      
#1B
try:
      target_path3=os.path.join(r"\\10.32.12.23\PVCTData\ClassA\2022_"+a)
      all_content3= os.listdir(target_path3)
      target_path4=os.path.join(r"\\10.32.12.23\PVCTData\ClassB\2022_"+a)
      all_content4= os.listdir(target_path4)
      
      
      print(r"1B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content3))),(int(len(all_content4))-1))
except:
      print(r"1B 2022_"+str(a)+" 时段A B级片数量为0 0")


      
#2A
try:
      target_path5=os.path.join(r"\\10.32.13.22\PVCTData\ClassA\2022_"+a)
      all_content5= os.listdir(target_path5)
      target_path6=os.path.join(r"\\10.32.13.22\PVCTData\ClassB\2022_"+a)
      all_content6= os.listdir(target_path6)
      
      print(r"2A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content5))),(int(len(all_content6))-1))
except:
      print(r"2A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#2B
try:
      target_path7=os.path.join(r"\\10.32.13.23\PVCTData\ClassA\2022_"+a)
      all_content7= os.listdir(target_path7)
      target_path8=os.path.join(r"\\10.32.13.23\PVCTData\ClassB\2022_"+a)
      all_content8= os.listdir(target_path8)
      
      print(r"2B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content7))),(int(len(all_content8))-1))
except:
      print(r"2B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#3A
try:
      target_path9=os.path.join(r"\\10.32.14.22\PVCTData\ClassA\2022_"+a)
      all_content9= os.listdir(target_path9)
      target_path10=os.path.join(r"\\10.32.14.22\PVCTData\ClassB\2022_"+a)
      all_content10= os.listdir(target_path10)
      
      print(r"3A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content9))),(int(len(all_content10))-1))
except:
      print(r"3A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#3B
try:
      target_path11=os.path.join(r"\\10.32.14.23\PVCTData\ClassA\2022_"+a)
      all_content11= os.listdir(target_path11)
      target_path12=os.path.join(r"\\10.32.14.23\PVCTData\ClassB\2022_"+a)
      all_content12= os.listdir(target_path12)
      
      print(r"3B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content11))),(int(len(all_content12))-1))
except:
      print(r"3B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#4A
try:
      target_path13=os.path.join(r"\\10.32.15.22\PVCTData\ClassA\2022_"+a)
      all_content13= os.listdir(target_path13)
      target_path14=os.path.join(r"\\10.32.15.22\PVCTData\ClassB\2022_"+a)
      all_content14= os.listdir(target_path14)
      
      print(r"4A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content13))),(int(len(all_content14))-1))
except:
      print(r"4A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#4B
try:
      target_path15=os.path.join(r"\\10.32.15.23\PVCTData\ClassA\2022_"+a)
      all_content15= os.listdir(target_path15)
      target_path16=os.path.join(r"\\10.32.15.23\PVCTData\ClassB\2022_"+a)
      all_content16= os.listdir(target_path16)
      
      print(r"4B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content15))),(int(len(all_content16))-1))
except:
      print(r"4B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#5A
try:
      target_path17=os.path.join(r"\\10.32.16.22\PVCTData\ClassA\2022_"+a)
      all_content17= os.listdir(target_path17)
      target_path18=os.path.join(r"\\10.32.16.22\PVCTData\ClassB\2022_"+a)
      all_content18= os.listdir(target_path18)
      
      print(r"5A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content17))),(int(len(all_content18))-1))
except:
      print(r"5A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#5B
try:
      target_path19=os.path.join(r"\\10.32.16.23\PVCTData\ClassA\2022_"+a)
      all_content19= os.listdir(target_path19)
      target_path20=os.path.join(r"\\10.32.16.23\PVCTData\ClassB\2022_"+a)
      all_content20= os.listdir(target_path20)
      
      print(r"5B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content19))),(int(len(all_content20))-1))
except:
      print(r"5B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#6A
try:
      target_path21=os.path.join(r"\\10.32.17.22\PVCTData\ClassA\2022_"+a)
      all_content21= os.listdir(target_path21)
      target_path22=os.path.join(r"\\10.32.17.22\PVCTData\ClassB\2022_"+a)
      all_content22= os.listdir(target_path22)
      
      print(r"6A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content21))),(int(len(all_content22))-1))
except:
      print(r"6A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#6B
try:
      target_path23=os.path.join(r"\\10.32.17.23\PVCTData\ClassA\2022_"+a)
      all_content23= os.listdir(target_path23)
      target_path24=os.path.join(r"\\10.32.17.23\PVCTData\ClassB\2022_"+a)
      all_content24= os.listdir(target_path24)
      
      print(r"6B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content23))),(int(len(all_content24))-1))
except:
      print(r"6B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#7A
try:
      target_path25=os.path.join(r"\\10.32.18.22\PVCTData\ClassA\2022_"+a)
      all_content25= os.listdir(target_path25)
      target_path26=os.path.join(r"\\10.32.18.22\PVCTData\ClassB\2022_"+a)
      all_content26= os.listdir(target_path26)
      
      print(r"7A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content25))),(int(len(all_content26))-1))
except:
      print(r"7A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#7B
try:
      target_path27=os.path.join(r"\\10.32.18.23\PVCTData\ClassA\2022_"+a)
      all_content27= os.listdir(target_path27)
      target_path28=os.path.join(r"\\10.32.18.23\PVCTData\ClassB\2022_"+a)
      all_content28= os.listdir(target_path28)
      
      print(r"7B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content27))),(int(len(all_content28))-1))
except:
      print(r"7B 2022_"+str(a)+" 时段A B级片数量为 0 0")


#8A
try:
      target_path29=os.path.join(r"\\10.32.19.22\PVCTData\ClassA\2022_"+a)
      all_content29= os.listdir(target_path29)
      target_path30=os.path.join(r"\\10.32.19.22\PVCTData\ClassB\2022_"+a)
      all_content30= os.listdir(target_path30)
      
      print(r"8A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content29))),(int(len(all_content30))-1))
except:
      print(r"8A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#8B
try:
      target_path31=os.path.join(r"\\10.32.19.23\PVCTData\ClassA\2022_"+a)
      all_content31= os.listdir(target_path31)
      target_path32=os.path.join(r"\\10.32.19.23\PVCTData\ClassB\2022_"+a)
      all_content32= os.listdir(target_path32)
      
      print(r"8B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content31))),(int(len(all_content32))-1))
except:
      print(r"8B 2022_"+str(a)+" 时段A B级片数量为 0 0")



      

#9A
try:
      target_path33=os.path.join(r"\\10.32.20.22\halm\PVCTData\ClassA\2022_"+a)
      all_content33= os.listdir(target_path33)
      target_path34=os.path.join(r"\\10.32.20.22\halm\PVCTData\ClassB\2022_"+a)
      all_content34= os.listdir(target_path34)
      
      print(r"9A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content33))),(int(len(all_content34))-1))
except:
      print(r"9A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#9B
try:
      target_path35=os.path.join(r"\\10.32.20.23\PVCTData\ClassA\2022_"+a)
      all_content35= os.listdir(target_path35)
      target_path36=os.path.join(r"\\10.32.20.23\PVCTData\ClassB\2022_"+a)
      all_content36= os.listdir(target_path36)
      
      print(r"9B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content35))),(int(len(all_content36))-1))
except:
      print(r"9B 2022_"+str(a)+" 时段A B级片数量为 0 0")

      


#10A
try:
      target_path37=os.path.join(r"\\10.32.21.22\PVCTData\ClassA\2022_"+a)
      all_content37= os.listdir(target_path37)
      target_path38=os.path.join(r"\\10.32.21.22\PVCTData\ClassB\2022_"+a)
      all_content38= os.listdir(target_path38)
      
      print(r"10A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content37))),(int(len(all_content38))-1))
except:
      print(r"10A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#10B
try:
      target_path39=os.path.join(r"\\10.32.21.23\PVCTData\ClassA\2022_"+a)
      all_content39= os.listdir(target_path39)
      target_path40=os.path.join(r"\\10.32.21.23\PVCTData\ClassB\2022_"+a)
      all_content40= os.listdir(target_path40)
      
      print(r"10B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content39))),(int(len(all_content40))-1))
except:
      print(r"10B 2022_"+str(a)+" 时段A B级片数量为 0 0")




#11A
try:
      target_path41=os.path.join(r"\\10.32.22.22\PVCTData\ClassA\2022_"+a)
      all_content41= os.listdir(target_path41)
      target_path42=os.path.join(r"\\10.32.22.22\PVCTData\ClassB\2022_"+a)
      all_content42= os.listdir(target_path42)
      
      print(r"11A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content41))),(int(len(all_content42))-1))
except:
      print(r"11A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#11B
try:
      target_path43=os.path.join(r"\\10.32.22.23\PVCTData\ClassA\2022_"+a)
      all_content43= os.listdir(target_path43)
      target_path44=os.path.join(r"\\10.32.22.23\PVCTData\ClassB\2022_"+a)
      all_content44= os.listdir(target_path44)
      
      print(r"11B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content43))),(int(len(all_content44))-1))
except:
      print(r"11B 2022_"+str(a)+" 时段A B级片数量为 0 0")
      





#12A
try:
      target_path45=os.path.join(r"\\10.32.23.22\PVCTData\ClassA\2022_"+a)
      all_content45= os.listdir(target_path45)
      target_path46=os.path.join(r"\\10.32.23.22\PVCTData\ClassB\2022_"+a)
      all_content46= os.listdir(target_path46)
      
      print(r"12A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content45))),(int(len(all_content46))-1))
except:
      print(r"12A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#12B
try:
      target_path47=os.path.join(r"\\10.32.23.23\PVCTData\ClassA\2022_"+a)
      all_content47= os.listdir(target_path47)
      target_path48=os.path.join(r"\\10.32.23.23\PVCTData\ClassB\2022_"+a)
      all_content48= os.listdir(target_path48)
      
      print(r"12B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content47))),(int(len(all_content48))-1))
except:
      print(r"12B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#13A
try:
      target_path49=os.path.join(r"\\10.32.24.22\PVCTData\ClassA\2022_"+a)
      all_content49= os.listdir(target_path49)
      target_path50=os.path.join(r"\\10.32.24.22\PVCTData\ClassB\2022_"+a)
      all_content50= os.listdir(target_path50)
      
      print(r"13A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content49))),(int(len(all_content50))-1))
except:
      print(r"13A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#13B
try:
      target_path51=os.path.join(r"\\10.32.24.23\PVCTData\ClassA\2022_"+a)
      all_content51= os.listdir(target_path51)
      target_path52=os.path.join(r"\\10.32.24.23\PVCTData\ClassB\2022_"+a)
      all_content52= os.listdir(target_path52)
      
      print(r"13B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content51))),(int(len(all_content52))-1))
except:
      print(r"13B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#14A
try:
      target_path53=os.path.join(r"\\10.32.25.22\PVCTData\ClassA\2022_"+a)
      all_content53= os.listdir(target_path53)
      target_path54=os.path.join(r"\\10.32.25.22\PVCTData\ClassB\2022_"+a)
      all_content54= os.listdir(target_path54)
      
      print(r"14A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content53))),(int(len(all_content54))-1))
except:
      print(r"14A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#14B
try:
      target_path55=os.path.join(r"\\10.32.25.23\PVCTData\ClassA\2022_"+a)
      all_content55= os.listdir(target_path55)
      target_path56=os.path.join(r"\\10.32.25.23\PVCTData\ClassB\2022_"+a)
      all_content56= os.listdir(target_path56 )
      
      print(r"14B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content55))),(int(len(all_content56))-1))
except:
      print(r"14B 2022_"+str(a)+" 时段A B级片数量为 0 0")



#15A
try:
      target_path57=os.path.join(r"\\10.32.26.22\PVCTData\ClassA\2022_"+a)
      all_content57= os.listdir(target_path57)
      target_path58=os.path.join(r"\\10.32.26.22\PVCTData\ClassB\2022_"+a)
      all_content58= os.listdir(target_path58)
      
      print(r"15A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content57))),(int(len(all_content58))-1))
except:
      print(r"15A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#15B
try:
      target_path59=os.path.join(r"\\10.32.26.23\PVCTData\ClassA\2022_"+a)
      all_content59= os.listdir(target_path59)
      target_path60=os.path.join(r"\\10.32.26.23\PVCTData\ClassB\2022_"+a)
      all_content60= os.listdir(target_path60)
      
      print(r"15B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content59))),(int(len(all_content60))-1))
except:
      print(r"15B 2022_"+str(a)+" 时段A B级片数量为 0 0")





#16A
try:
      target_path61=os.path.join(r"\\10.32.27.22\PVCTData\ClassA\2022_"+a)
      all_content61= os.listdir(target_path61)
      target_path62=os.path.join(r"\\10.32.27.22\PVCTData\ClassB\2022_"+a)
      all_content62= os.listdir(target_path62)
      
      print(r"16A 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content61))),(int(len(all_content62))-1))
except:
      print(r"16A 2022_"+str(a)+" 时段A B级片数量为 0 0")
#16B
try:
      target_path63=os.path.join(r"\\10.32.27.23\PVCTData\ClassA\2022_"+a)
      all_content63= os.listdir(target_path63)
      target_path64=os.path.join(r"\\10.32.27.23\PVCTData\ClassB\2022_"+a)
      all_content64= os.listdir(target_path64)
      
      print(r"16B 2022_"+str(a)+" 时段A B级片数量为",(int(len(all_content63))),(int(len(all_content64))-1))
except:
      print(r"16B 2022_"+str(a)+" 时段A B级片数量为 0 0")













#count_num=-1
#for content in all_content:
#      if os.path.isdir(target_path+content):
#          all_sub_content=os.listdir(target_path+content)
          









          
