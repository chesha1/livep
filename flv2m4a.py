import os

# Only input para
path = 'C:\\files\\record\\25846913-一只清钰'



files = os.listdir(path)  # 录制-25846913-20221120-083923-467-【新v】早上的赛博小狼.flv
files_abs = []  # C:\\files\\record\\25846913-一只清钰\\录制-25846913-20221120-083923-467-【新v】早上的赛博小狼.flv
for i in files:
    files_abs.append(os.path.join(path, i))
files_flv = []  # C:\\files\\record\\25846913-一只清钰\\录制-25846913-20221120-083923-467-【新v】早上的赛博小狼.flv
files_raw = []  # 录制-25846913-20221120-083923-467-【新v】早上的赛博小狼
for i in files_abs:
    if os.path.splitext(i)[-1] == '.flv':
        files_flv.append(i)
        files_raw.append(os.path.splitext(i)[0].split('\\')[-1])

for i in range(len(files_flv)):
    out = os.system("ffmpeg -i " + files_flv[i] + " -vn -c:a copy " + path+"\\"+files_raw[i] + ".m4a")

for i in files_flv:
    os.remove(i)

