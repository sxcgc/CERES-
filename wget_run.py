import yaml
import datetime
import os
first_path = os.getcwd()



data_email = yaml.load(open('track_change.yaml'))
data_message = yaml.load(open('message.yaml'))

path_all = data_message

for keyword in path_all.keys():
    for dirfile in path_all[keyword]:
        if(os.path.exists(keyword+'/'+dirfile) == False):
            os.makedirs(keyword+'/'+dirfile)
            print(keyword+'/'+dirfile +' was created')

#print(data_message)
f_sh = open('wget_input.sh','w')
f_error = open('download_aqua_error','w')
timedelta = datetime.timedelta(days=1)
dmin = datetime.datetime.now()
for dkey in data_message:
    print(dkey)
    f_error.writelines(dkey + '\r\n')
    for d in data_message[dkey]:
        ddate = datetime.datetime.strptime(d[:], '%Y-%m-%d')
        flag = 1
        for key in data_email.keys():
            email = data_email[key]
            for e in email:
                edate = datetime.datetime.strptime(e[40:50],'%Y%m%d%H%M')
                if (dmin > edate):
                    dmin = edate
                if(ddate+timedelta > edate and ddate-timedelta < edate):
                    flag = 0
                    f_sh.writelines('axel -n 10 -o ./'+ dkey+'/' + d + '/'+ '  ftp://xfr140.larc.nasa.gov/'+key+'/'+e[0:50]+' \n')
        if (flag == 1):
            f_error.writelines(d + ' no\r\n')
        else:
            f_error.writelines(d + ' yes\r\n')
print(dmin)
f_error.close()
f_sh.close()
        
