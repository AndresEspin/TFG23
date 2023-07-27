import sys
sys.path.append('.')
from utils.gdrive import GDriveUtil, GDriveHost



HOST=GDriveHost.SHARED_WITH_ME # or GDriveHost.MINE
FILE_LOCATION_PATH="/TFG"

csvfile1="daily_sessions_report20221110-1-141xfwr.csv"
rptfile1="AltresServeisClaret.rpt"
xlsfile1="MASTER.xls"

gdrive=GDriveUtil()

df1=gdrive.getCSVFileAsDF(
    fileFQN = f"{HOST}:{FILE_LOCATION_PATH}/{csvfile1}",
    sep=";",
    header=1)
    
print(f"----------CSV file :{csvfile1}----------")
print(df1.head())

df2=gdrive.getRPTFileAsDF(
    fileFQN = f"{HOST}:{FILE_LOCATION_PATH}/{rptfile1}",
)
print(f"----------RTP file :{csvfile1}----------")
print(df2.head())


df3=gdrive.getXLSFileAsDF(
    fileFQN = f"{HOST}:{FILE_LOCATION_PATH}/{xlsfile1}",
)
print(f"----------XLS file :{csvfile1}----------")
print(df3.head())
