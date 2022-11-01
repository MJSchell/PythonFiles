import datetime
import gspread
import gspread_formatting
import string
import cv2

#AM/PM SpreadSheet
#Time
#School
#Decypher School
#If someone uses an incorrect QRcode

#pip install gspread
#pip install gspread-formatting
#pip install qrcode
#pip install Pillow
#pip install opencv-python

#Spreadsheet -> Overall Project File
#Worksheet -> Individual sub files in the sheet
#Cell -> Little Squares on the Worksheet to store data

#A worksheet is a just single-page data file that is generally created as a specific data file, while a spreadsheet is a whole program where the user can create a worksheet. A spreadsheet is a bundle of worksheets where generally one or more than one worksheet is available.

#Private Key to access the google spreadsheet using a "Service Account" AKA Script/Third Party
credentials = {
    #Deleted Purposefully
}

#sa=serivceaccount
sa = gspread.service_account_from_dict(credentials)
# ServiceAccount open ("GoogleSpreadsheetName")
sh = sa.open("PythonToGoogleSheets")

alphabet = list(string.ascii_uppercase)
dayOfWeekList = ['Sunday', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#Required to get the first Worksheet
today = datetime.date.today()
month = today.strftime("%B")
year = today.strftime("%Y")


#Formatting
boldFormat = gspread_formatting.CellFormat(
    textFormat=gspread_formatting.TextFormat(
        bold=True, foregroundColor=gspread_formatting.Color(0, 128, 128)),
    horizontalAlignment="CENTER"
)
italicFormat = gspread_formatting.CellFormat(
    textFormat=gspread_formatting.TextFormat(
        italic=True, foregroundColor=gspread_formatting.Color(110, 114, 174)),
    horizontalAlignment="CENTER"
)
normalFormat = gspread_formatting.CellFormat(
    horizontalAlignment="CENTER"
)
normalBoldFormat = gspread_formatting.CellFormat(
    textFormat=gspread_formatting.TextFormat(
        bold=True),
    horizontalAlignment="CENTER"
)
lateFormat = gspread_formatting.CellFormat(
    backgroundColor=gspread_formatting.Color(1, 1, 0),
    horizontalAlignment="CENTER"
)
presentFormat = gspread_formatting.CellFormat(
    backgroundColor=gspread_formatting.Color(0, 1, 0),
    horizontalAlignment="CENTER"
)
AbsentFormat = gspread_formatting.CellFormat(
    backgroundColor=gspread_formatting.Color(1, 0, 0),
    horizontalAlignment="CENTER"
)

#gets the current values in the Worksheet into a List of Lists


def getCurrentWorksheetList():
    global worksheetlist
    #Getting all the Values into a list of lists so Python runs faster and less requests to the Google API
    worksheetlist = wks.get_all_values()

#Grabs the current Date and Time of the OS


def GetCurrentDateTime():
    print("Got new DateTime")
    global today
    global month
    global monthnumber
    global year
    global day
    global dayofWeek
    global currentTime
    today = datetime.date.today()
    time = datetime.datetime.now()
    #Month Name (October)
    month = today.strftime("%B")
    #Month Number (1-12)
    monthnumber = today.strftime("%m")
    #Year Number (2022)
    year = today.strftime("%Y")
    #day (1-31)
    day = today.strftime("%d")
    #day of week (Sunday - Saturday)
    dayofWeek = today.strftime("%w")
    #current time function is in military time (00:00 - 23:59)
    #Normal time for reference                 (12:00 AM - 11:00 PM)
    currentTime = time.strftime("%H:%M")
    getCurrentWorksheetList()

#Tries to get the current work Worksheet using the current month (Fail: New Worksheet; Pass:Grabs the current Worksheet)


def GetCurrentWorksheet():
    global wks
    #Tries to get the current Worksheet using the current month
    try:
        #Pass:Grabs the current Worksheet
        wks = sh.worksheet(str(month+year))
        return True
    except:
        #Fail: New Worksheet
        NewSheet()

#Generates a new day


def NewDay():
    print("Setting new day")
    #Checks to see if the New day is in the current month (Y : closes function and runs new Worksheet N: Runs NewDay Function)
    if GetCurrentWorksheet():
        #Setting users who didn't clock in on pervious day to absent
        for i in range(len(worksheetlist)):
            if worksheetlist[i][-1] == "":
                wks.update_cell(i+1, len(worksheetlist[i]), 'Absent')
                gspread_formatting.format_cell_ranges(
                    wks, [(alphabet[len(worksheetlist[i])-1]+str(i+1), AbsentFormat)])
        #Creates the new Day and Day of the week on the current Worksheet
        i = len(worksheetlist[0])+1
        wks.update_cell(1, i, monthnumber+"/"+day)
        wks.update_cell(2, i, dayOfWeekList[int(dayofWeek)])
        gspread_formatting.format_cell_ranges(
            wks, [(alphabet[i-1]+"1", boldFormat), (alphabet[i-1]+"2", italicFormat)])
        getCurrentWorksheetList()

#Creates new Worksheet (MonthYear)


def NewSheet():
    print("Making new Worksheet")
    global wks
    #Generating the Worksheet
    wks = sh.add_worksheet(title=str(month+year), rows=50, cols=36)
    #Generates the Static (Same across all Worksheet) "Cells" on the Worksheet
    wks.update_cell(1, 1, 'Class Name')
    wks.update_cell(1, 2, 'Teacher Name')
    wks.update_cell(2, 1, 'ID')
    wks.update_cell(2, 2, 'Name')
    gspread_formatting.format_cell_ranges(
        wks, [("A1:B2", normalBoldFormat)])
    GetCurrentDateTime()
    NewDay()

#Checks to see if a new day is to be generated or not


def CheckNewDay():
    print("Checking new day")
    #checks to see if the newest entry for the day is equal to the current day (monthnumber/day != or == currentmonthnumber/currentday)
    if (worksheetlist[0][-1] != monthnumber+"/"+day):
        NewDay()

#if the user clocks in on the 2nd but not the first it doesn't mark the user as absent on the first. This is that fix


def AbsentBugFix():
    print("Running Absent Bug Fix")
    getCurrentWorksheetList()
    #Checks to see if there are No entries in cell (No entry = "") for user's current row
    for i in range(len(worksheetlist[-1])):
        if worksheetlist[-1][i] == "":
            #Generates cell to be absent if there is no entry
            wks.update_cell(len(worksheetlist), i+1, "Absent")
            gspread_formatting.format_cell_ranges(
                wks, [(alphabet[i]+str(len(worksheetlist)), AbsentFormat)])


def ClockIn(id, name):
    #if the user is found
    found = False
    print("Clocking In")
    GetCurrentDateTime()
    CheckNewDay()
    print("Past Checks")
    #Searches for the user and if found marks as present
    for i in range(len(worksheetlist)):  # i is col
        #checks to see if the user's ID is in the First column
        if (worksheetlist[i][0]) == id:
            print("IsInWorksheet")
            z = len(worksheetlist[0])
            #Check so see if user is late
            #if between 07:31 to 10:59 or Greater than 11:40 is late
            if int(currentTime[0:2]) > 11 or int(currentTime[0:2]) == 11 and int(currentTime[3:5]) > 40 or int(currentTime[0:2]) > 7 and int(currentTime[0:2]) < 11 or int(currentTime[0:2]) == 7 and int(currentTime[3:5]) > 30:
                print("late")
                wks.update_cell(i+1, z, 'Late')
                formatting = lateFormat
            else:
                #Everything else is considered present
                wks.update_cell(i+1, z, 'Present')
                formatting = presentFormat
            gspread_formatting.format_cell_ranges(
                wks, [(alphabet[len(worksheetlist[0])-1]+str(i+1), formatting)])
            print("Found is True")
            found = True
            break
#Adds the User if They arn't found
    if found == False:
        print("Found is False")
        i = len(worksheetlist)+1  # i is the end of the column A
        #sets the id (column A) and Name (column B)
        wks.update_cell(i, 1, id)
        wks.update_cell(i, 2, name)
        gspread_formatting.format_cell_ranges(
            wks, [("A"+str(i)+":B"+str(i), normalFormat)])
        #reruns function to actually mark if user is late or present
        ClockIn(id, name)
        #Read Function Description
        AbsentBugFix()
    else:
        qrCam()


def read_qr_code(value):
  try:
      ID = value[0:value.index(",")]
      Name = value[value.index(",")+1:]
      ClockIn(ID, Name)
  except:
      print("Unable To Read Code")
      qrCam()


def qrCam():
    vid = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        print(frame)
        if cv2.waitKey(1) & len(data) > 0:
          print(data)
          break
        cv2.imshow('frame', frame)
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    read_qr_code(data)


#Required to run any function
GetCurrentWorksheet()

qrCam()
