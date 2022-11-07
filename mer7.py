# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

import json
a={"name":"Abhishek","Designation":"CEO of navgurukul","Gender":"Mela","Age":29}
with open("abhishek . json","w")as g:
    json.dump(a,g,indent=12)



    