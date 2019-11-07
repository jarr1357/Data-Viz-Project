from win32com.client.dynamic import Dispatch  
import time  
  
PL = Dispatch("PISDK.PISDK")  
print("PISDK Version:", PL.PISDKVersion)  
print("Known Server List")  
print("-----------------")  
  
for server in PL.Servers:      
    if server.Name == PL.Servers.DefaultServer.Name:      
        print("{0}\t:: DEFAULT::".format(server.Name))  
    else:      
        print(server.Name)  
    tag = server.PIPoints("WCHPCOGEN_ACW.COGEN1.UTILITY.KW.PRESENT_VALUE")
    print("\t", tag.PointAttributes("tag").Value)      
    print("\t", tag.Data.Snapshot.Value)  
    timestamp = time.localtime(tag.Data.Snapshot.TimeStamp.UTCseconds)  
    print("\t", time.asctime(timestamp)) 
