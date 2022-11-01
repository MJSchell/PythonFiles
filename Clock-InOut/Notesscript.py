import datetime
import gspread
import gspread_formatting
import qrcode
import cv2
credentials = {
}


#sa=serivceaccount
# sa=gspread.service_account_from_dict(credentials)
# sa=gspread.service_account(filename="C:\Users\Stormtroopes\Documents\GitHub\Clock-IO\credentialsfile.json") #for if you store the file in the current directory
# sa=gspread.service_account() #for if you store the file in the gspread directory
#sh=sheet
# sh = sa.open("PythonToGoogleSheets") #ServiceAccount open ("GoogleSheetsName")

# wks = sh.worksheet("October2022")

# print('Rows: ',wks.row_count)   #print out row count
# print('Cols: ', wks.col_count)  #print out column count

# print(wks.acell("A1").value)  #Get the value of a cell
# print(wks.cell(1,1).value)     #Get the value of a cell with row, then column

# print(wks.get('A1:H1'))     #Get the value of a range

# print(wks.get_all_records()) #dictionary
# print(wks.get_all_values()) #list of lists

# worksheet.update_cell(1, 2, 'Bingo!') #update cell by row and column

# wks.update("A2:B3",[["T", "est9"],["Tt99", "10"]]) #update cell range
# fmt = gspread_formatting.CellFormat(
#   textFormat=gspread_formatting.TextFormat(bold=True, foregroundColor=gspread_formatting.Color(0,128,128)),
#   horizontalAlignment="CENTER"
# )

# gspread_formatting.format_cell_ranges(wks, [(1,2, fmt)])

# for i in range(1,wks.row_count+1):
#   print(i)
# for i in range(1,wks.col_count+1):
#   print(i)
# today = datetime.datetime.now()
# currentTime= today.strftime("%H:%M")
# print(currentTime[3:5])

# def isTrue():
#   i=0
#   if i ==0:
#     return True

# if isTrue():
#   print("Hello")
# else:
#   print("Not Hello")

# img = qrcode.make("1,Mason")
# image_path = "Downloads"
# img.save(f"{image_path}/QRcode.jpg")

# def read_qr_code(filename):
#   try:
#       ID=""
#       img = cv2.imread(filename)
#       detect = cv2.QRCodeDetector()
#       value, points, straight_qrcode = detect.detectAndDecode(img)
#       for i in value:
#         if i == ",":
#           Name=value[value.index(i)+1:len(filename)]
#           break
#         else:
#           ID+=i
#       return ID , Name
#   except:
#       print("Unable To Read Code")
#       read_qr_code()
      
# print(read_qr_code("Downloads\QRcode.jpg"))

def qrCam():
    vid = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
      # Capture the video frame by frame
      ret, frame = vid.read()
      data, bbox, straight_qrcode = detector.detectAndDecode(frame)
      if cv2.waitKey(1) & len(data) > 0:
          print(data)
          break
      cv2.imshow('frame', frame)
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

qrCam()

