import socket

HOST_NAME = 'node2.cs.arizona.edu'
PORT_NUMBER = 9000 # Maybe set this to 9000.

if __name__ == '__main__':
    hstname = socket.getfqdn()
    addr, abc, lis = socket.gethostbyname_ex(HOST_NAME)
    print 'list size %d \n',len(lis)
    print 'The address of ', hstname, 'is', lis

