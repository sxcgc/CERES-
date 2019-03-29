import yaml
import datetime
import os
#first_path = os.getcwd()

device = 4

f_sh ={}
for i in range(4):
    f_sh[str(i)] = open('wget_input_'+srt(i)+'.sh','w')
	
data_email = yaml.load(open('track_change.yaml'))
data_message = yaml.load(open('message.yaml'))

path_all = data_message

for keyword in path_all.keys():
    for dirfile in path_all[keyword]:
        if(os.path.exists(keyword+'/'+dirfile) == False):
            os.makedirs(keyword+'/'+dirfile)
            print(keyword+'/'+dirfile +' was created')

#print(data_message)
f_error = open('download_aqua_error','w')
flag = 0
timedelta = datetime.timedelta(days=1)
index = 0

for key in data_email.keys():
    email = data_email[key]
    for dkey in data_message:
        for d in data_message[dkey]:
            ddate = datetime.datetime.strptime(d[:],'%Y-%m-%d')
            for e in email:
                edate = datetime.datetime.strptime(e[40:48],'%Y%m%d')
                if(ddate == edate):
                    flag = 1
					index = index +1
            if(flag == 1):
                flag = 0
                f_error.writelines(d + ' no\r\n')

for i in range(device):
    for j in range(index/device):
        f_sh[srt(i)].writelines('wget ./'+ dkey+'/' + d + '/'+ ' ftp://xfr140.larc.nasa.gov/'+key+'/'+e[0:50]+'\r\n')

for i in range(device):
    f_sh[str(i)].close()
#f_sh.writelines('wget ./'+ dkey+'/' + d + '/'+ ' ftp://xfr140.larc.nasa.gov/'+key+'/'+e[0:50]+'\r\n')
f_error.close()
#f_sh.close()
f = open('run.sh','w')

for i in range(device):
    f.writelines('chmod 701 wget_input_*.sh')

f.close()



        
