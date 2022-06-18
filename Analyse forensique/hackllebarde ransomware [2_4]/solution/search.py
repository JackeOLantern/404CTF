import re

#regex = "\[\d* \d* \d* \d*\]$"
regex = "([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))(?<!127)(?<!^10)(?<!^0)\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!192\.168)(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
SearchFunction = re.compile(regex)

f = open('strings.txt','r', encoding='utf-8')
f2 = open('evil_dialog.txt','w')
f3 = open('evil_http.txt','w')
# You check if the pattern matches for each line. This won't load the entire file to the memory:
count = 1000
for line in f:
    if 'Malveillant' in line or 'EVIL-SERV' in line or '192.168.61.137' in line or '38088' in line:
        # print(line.strip())
        f2.write(line)
    else:
        if 'http' in line:
            if 'dailymotion' in line  or 'trivago' in line  or 'snap' in line  or 'fonts' in line  or '.net' in line or 'twitter' in line or '.goog' in line or 'gnome' in line or '.org' in line or 'github' in line or 'google' in line or 'leboncoin' in line or 'youtube' in line or 'amazon' in line or 'wikipedia' in line or 'letsencrypt' in line or 'digicert' in line  or 'mozilla' in line or 'ubuntu' in line:
                continue
            f3.write(line)
        continue
    result = re.search(SearchFunction, line)
    if result is not None:
        if not 'xxxxgithub' in line or 'google' in line or 'leboncoin' in line or 'youtube' in line or 'amazon' in line or 'wikipedia' in line or 'function' in line or '-icon' in line  or 'font-' in line or 'xmlns' in line:
            continue
        print(line)
        count = count - 1
        if count <=0:
            break
f.close()