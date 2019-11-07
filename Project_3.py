import sys  
import clr  
  
  
sys.path.append(r'C:\Program Files (x86)\PIPC\AF\PublicAssemblies\4.0')    
clr.AddReference('OSIsoft.AFSDK')  
  
  
from OSIsoft.AF import *  
from OSIsoft.AF.PI import *  
from OSIsoft.AF.Asset import *  
from OSIsoft.AF.Data import *  
from OSIsoft.AF.Time import *  
from OSIsoft.AF.UnitsOfMeasure import *

piServers = PIServers()    
piServer = piServers.DefaultPIServer;  

pt = PIPoint.FindPIPoint(piServer, "WCHPCOGEN_ACW.COGEN1.UTILITY.KW.PRESENT_VALUE")  
name = pt.Name.lower() 

timerange = AFTimeRange("19/11/05 11:56 PM", "19/11/06 2:53 AM")  
recorded = pt.RecordedValues(timerange, AFBoundaryType.Inside, "", False)  
print('\nShowing PI Tag RecordedValues from {0}'.format(name))  
for event in recorded:  
  print('{0} value: {1}'.format(event.Timestamp.LocalTime, event.Value))
