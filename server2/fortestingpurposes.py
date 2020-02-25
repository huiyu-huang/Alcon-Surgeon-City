

#sys.path.insert(0,'ml/test.py')
import pyPDF2
#os.rmdir("static/"+"1")
#os.makedirs("static/"+"1")
#os.makedirs("5")
#os.rmdir("5")
#value = "guest"
#shutil.copy("static/" + "1" + "/surgery1clip.mp4", "static/" + "1/" + "harvard.mp4") 

##with open("guest.txt","r") as f:
##    print(f.read())
##    
##    if 'tomato' in f.read():
##        print("true")
##    #f.write("yes")
##
## 
##f.close() 


# save FPDF() class into  
# a variable pdf 
pdf = FPDF()    
   
# Add a page 
pdf.add_page() 
   
# set style and size of font  
# that you want in the pdf 
pdf.set_font("Arial", size = 15) 
  
# open the text file in read mode 
f = open("guest.txt", "r") 
  
# insert the texts in pdf 
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
   
# save the pdf with name .pdf 
pdf.output("mygfg.pdf")  
