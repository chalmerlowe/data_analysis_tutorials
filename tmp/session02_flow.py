hostname = 'mylaptop'
num_hosts = 42
myhost = input('provide a computer name: ')

if hostname == myhost:
    print('hostnames are equal')

count = input('provide a number: ')
count = int(count)
if count > num_hosts:
    print('count exceeds number of hours')
elif count < num_hosts:
    print('count is less than number of hosts')
else:
    print('count equals number of hosts')
