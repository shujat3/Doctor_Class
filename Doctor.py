import management

# doctor class to hold information of particular doctor
class Doctor:
    id = 0
    name = ""
    speciality = ""
    timing = ""
    qualification = ""
    roomNumber = 0
    # list to maintain all doctors
    doctor_list = []
    
    def __init__(self, id, name, speciality, timing, qualification, roomNumber):
        self.id = id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.roomNumber = roomNumber
        self.doctor_list.append(self)       # whenever a constructor is called the doctor is appending the list of doctors

    # function to convert the doctor's information according to the format of doctor.txt file    
    def formatDrInfo(self):
        formatted_data =  str(self.id) + '_' + self.name + '_' + self.speciality + '_' + self.timing + '_' + self.qualification + '_' + str(self.roomNumber)
        return formatted_data

    # this function takes information about a doctor and returns its object 
    def enterDrInfo(self):
        id = int(input("Enter the doctor's ID: "))
        name = input("Enter the doctor's name: ")
        speciality = input("Enter the doctor's speciality: ")
        timing = input("Enter the doctor's timings (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualifications: ")
        roomNumber = int(input("Enter the doctor's room number: "))
        return Doctor(id, name, speciality, timing, qualification, roomNumber)
        
    # this function reads the doctors' information from the given file
    def readDoctorsFile(self):
        f = open("doctors.txt", "r")
        next(f)  # skips the header of the file 
        lines = f.readlines()
        for line in lines: # reading the file line by line
            id, name, speciality, timing, qualification, roomNumber = line.split('_')   # splitting the contents of the line and saving to variables
            Doctor(int(id), name, speciality, timing, qualification, int(roomNumber))   # creating the doctor's object using the extracted info
        f.close()                                               
        for doc in self.doctor_list:
            if doc.id == self.id:
                print(doc.id, self.id)
                # print("Doctor with the same ID already exists\n")
                self.doctor_list.remove(doc)                                            # removing the doctor with the same id 

    # function to search for a doctor using his/her id 
    def search_doctor_id(self):             
        found = False
        search = int(input("Enter the doctor's ID to search: "))
        f = open("doctors.txt", "r")
        header = (f.readline())
        id, name, speciality, timing, qualification, roomNumber = header.split('_')
        print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))    # displaying the header
        
        # searching for doctor in file
        lines = f.readlines()                                                                                            
        for line in lines:
            did, name, speciality, timing, qualification, roomNumber = line.split('_')
            if did == str(search):
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(did,name,speciality,timing,qualification,roomNumber))   # displaying the doctor's info in a tabular format
                f.close()
                found = True

        # searching for doctor in the list of doctors
        for doc in self.doctor_list:
            if doc.id == id:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(doc.id,doc.name,doc.speciality,doc.timing,doc.qualification,doc.roomNumber))
                found = True
        if found == False:
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius menu\n")
        
    # search doctor by name
    def search_doctor_name(self):
        found = False
        search = input("Enter the doctor's name to search: ")
        f = open("doctors.txt", "r")
        header = (f.readline())
        id, name, speciality, timing, qualification, roomNumber = header.split('_')
        print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))
        
        # searching in file
        lines = f.readlines()
        for line in lines:
            id, dname, speciality, timing, qualification, roomNumber = line.split('_')
            if dname == search:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,dname,speciality,timing,qualification,roomNumber))
                f.close()
                found = True
        
        # searching in doctor's list
        for doc in self.doctor_list:
            if doc.name == name:
                print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(doc.id,doc.name,doc.speciality,doc.timing,doc.qualification,doc.roomNumber))
                found = True
        if found == False:   
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius menu\n")


    # display the information of the doctor using its object 
    def displayDoctorInfo(self):
        print(self.id)
        print(self.name)
        print(self.speciality)
        print(self.timing)
        print(self.qualification)
        print(self.roomNumber)
    
    # function to edit the information about a doctor using his/her id
    def edit_doctor(self):
        flag = False
        self.readDoctorsFile()  # readint the doctors.txt file and saving all doctors in the list 
        search = int(input("Please enter the id of the doctor that you want to edit their information:  "))
        for doc in self.doctor_list:
            if doc.id == search:        # if the doctor's id is found the program asks for further information to be changed
                flag = True             # set the flag to true 
                print("Enter new Name:")
                name = input("Enter the new name of the doctor: ")
                speciality = input("Enter new Specilist in: ")
                timing = input("Enter new Timing: ")
                qualification = input("Enter new Qualification:  ")
                roomNumber = int(input("Enter new Room number:  "))
                doc.name = name
                doc.speciality = speciality
                doc.timing = timing
                doc.qualification = qualification
                doc.roomNumber = roomNumber
                self.writeListofDoctorsToFile()         # write the changes to the file 
                break
        if flag==False:
            print("Cant find the doctor with the same ID on the system\n")
        else:
            print("Back to the prevoius Menu\n")

    # this function prints all the doctors that are present in the given file
    def list_doctors(self):
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            id, name, speciality, timing, qualification, roomNumber = line.split('_')
            print("{:<4} {:<20} {:<15} {:<15} {:<15} {:<15}".format(id,name,speciality,timing,qualification,roomNumber))
        f.close()
        print("Back to the prevoius menu\n")

    # this function reads the doctor's list from the program's memory and copy all doctors to file in the same format
    def writeListofDoctorsToFile(self):
        f = open("doctors.txt", "w")
        f.write("id_name_speciality_timing_qualification_roomNumber") # manually writing the header to the txt file
        for doc in self.doctor_list:    
            f.write("\n"+doc.formatDrInfo())
        f.close()
    
    # add a single doctor's information to the txt file
    def addDrToFile(self):
        new = self.enterDrInfo()
        f = open("doctors.txt", "a")
        f.write("\n"+new.formatDrInfo())
        f.close()
        print("Back to the prevoius menu\n")

    def doctor_menu(self):
        while 1:
            print("\nDoctors Menu:")
            print("1 - Display Doctors list")
            print("2 - Search for doctor by ID")
            print("3 - Search for doctor by name")
            print("4 - Add doctor")
            print("5 - Edit doctor info")
            print("6 - Back to the Main Menu")
        
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.list_doctors()
            elif choice == 2:
                self.search_doctor_id()
            elif choice == 3:
                self.search_doctor_name()
            elif choice == 4:
                self.addDrToFile()
            elif choice == 5:
                self.edit_doctor()
            elif choice == 6:
                management.Management.DisplayMenu()
            else:
                print("Invalid choice")
