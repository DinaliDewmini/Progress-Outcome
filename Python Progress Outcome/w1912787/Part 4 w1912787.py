# Date - 16/04/2022
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# UoW Student ID - w1912787
# IIT student ID - 20210017
# Name- Dinali Dewmmini



#----------------  MAIN FUNCTION  -----------------
    
def main():

#initializing the variables

    Pass=0
    Defer=0
    Fail=0
    Total=0
    Credits=[0,20,40,60,80,100,120]
    
#getting marks
    try:
        Pass= int(input("\nPlease enter credits at pass:"))
        if Pass not in Credits :
                print ("out of range")
                main()
                
        else:
            Defer= int(input("Please enter credits at defer:"))
            if Defer not in Credits:
                print ("out of range")
                main()
            else:
                Fail= int(input("Please enter credits at fail:"))
                if Fail not in Credits:
                    print ("out of range")
                    main()
                    
#checking for errors                    
    except ValueError:
         print("Integer required")
         
    inputs=(Pass,Defer,Fail)
    Total=Pass+Defer+Fail
    if Total !=120:
        print("Total incorrect")
        main()
        
#displaying the appropriate progression outcome
    elif Pass==120 and Defer==0 and Defer in Credits and Fail==0 and Fail in Credits:
                print("Progress")
                progress.append (inputs)              
    elif Pass>=100 and Defer<=20 and Defer in Credits and Fail<=20 and Fail in Credits:
                print("Progress(module trailer)")
                trailing.append (inputs)            
    elif Pass==40 and Defer==0 and Defer in Credits and Fail==80 and Fail in Credits:
                print("Exclude")
                exclude.append (inputs)           
    elif Pass==20 and Defer<=20 and Defer in Credits and Fail<=100 and Fail>=80 and Fail in Credits:
                print("Exclude")
                exclude.append (inputs)        
    elif Pass==0 and Defer<=40 and Defer in Credits and Fail<=120 and Fail>=80 and Fail in Credits:
                print("Exclude")
                exclude.append (inputs)      
    elif Pass<=80 and Pass>=40 and Defer<=80 and Defer in Credits and Fail<=60 and Fail in Credits:
                print("Do not progress – module retriever")
                module_retriever.append (inputs)    
    elif Pass==20 and Defer<=100 and Defer>=40 and Defer in Credits and Fail<=60 and Fail in Credits:
                print("Do not progress – module retriever")
                module_retriever.append (inputs)
    elif Pass==0 and Defer<=120 and Defer>=60 and Defer in Credits and Fail<=60 and Fail in Credits:
                print("Do not progress – module retriever")
                module_retriever.append (inputs)

#asking for another round
    if version.upper() == "SM":
         next()

         
# --------------  FUNCTION FOR HISTOGRAM PRINTING OR ASKING FOR ANOTHER ROUND  ----------------
def next():
    
    again=input("\nWould you like to enter another set of data?\nEnter 'Y' for yes or 'Q' to quit and view results:")  
    if again.upper() == "Y":
        main()
    elif again.upper() == "Q":
            

#Horizontal Histogram
            print("--------------------------------------------------------------")
            print("\n""HORIZONTAL HISTOGRAM ")
            print ("Progress",len(progress),":",len(progress)*"   *  ")
            print("Trailer",len(trailing),":",len(trailing)*"   *  ")
            print("Retriever",len(module_retriever),":",len(module_retriever)*"   *  ")
            print("Excluded",len(exclude),":",len(exclude)*"   *  ")
            print("\n" ,(len(progress))+(len(trailing))+(len(module_retriever))+(len(exclude)),"outcomes in total. ")
            print("\n""---------------------------------------------------------")
            

#Vertical Histogram
            print ("\n""VERTICAL HISTOGRAM")
            max_=max((len(progress)),(len(trailing)),(len(module_retriever)),(len(exclude)))
            print ("Progress","","Trailing","","  Retriever","","exclude")
            for x in range(max_):
                print("   {0}          {1}             {2}           {3}".format(
                    '*' if x < (len(progress))else ' ',
                    '*' if x < (len(trailing)) else ' ',
                    '*' if x < (len(module_retriever))else ' ',
                    '*' if x < (len(exclude)) else ' '))

            print("\n" ,(len(progress))+(len(trailing))+(len(module_retriever))+(len(exclude)),"outcomes in total. ")
            print("\n""-----------------------------------------------------------")
            print("")

#saving input progression data to a text file

            for w in progress:
                print("\n" +"progress,",w, file = open("histogram.txt","w"))  
            for x in trailing:
                print("trailing,",x, file = open("histogram.txt","a"))
            for y in module_retriever:
                print("module retriever,",y, file = open("histogram.txt","a"))              
            for z in exclude:
                print("exclude,",z, file = open("histogram.txt","a"))
                
#printing the textfile
            file=open("histogram.txt","r")
            for lines in file.readlines():
                print (lines)
            file.close()
            
    else:
        print("sorry,invalid character")
        next()

            
        
#-----------------------   MAIN PROGRAM  ---------------------------------   
trailing=[]
module_retriever=[]
exclude=[]         
progress=[]

# --------------  FUNCTION FOR ASK THE VERSION  ----------------
def versions():


    if version.upper() == "SM":
        print("\nStaff Version with Histogram ")
        main()
    elif version.upper() == "S":
        print("\nStudent Version ")
        main()
    else:
        print ("Invalid option")
 






#THE BEGINNING OF THE CODE
version=input("If you are a staff member please enter SM\nIf you are a student please enter S\nEnter a Version: ")
versions()


