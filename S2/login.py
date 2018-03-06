from getpass import getpass

tai_khoan = 'c4e'
password = 'c4e'

nhap_ten_dang_nhap = input('user_name:')
pswd = getpass('password:')

if nhap_ten_dang_nhap == tai_khoan and pswd == password:
    print('welcome back c4e')
elif nhap_ten_dang_nhap != tai_khoan or pswd != password:
    print ('cut!')
