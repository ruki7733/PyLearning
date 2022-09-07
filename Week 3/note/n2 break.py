sites=['google','baidu','taobao','ibm','qq']
for site in sites:
    if site=='ibm':
        print('ok')
        break
    print('site;'+site)
else:
    print('no break')
print('done')