# câu 7.3:
tệp = mở ( "tep.txt" , "r" )
a = tập tin . đọc ()
in ( "noi dung file la:" , a )
tập tin . đóng ()
# câu 7.7:
tệp = mở ( "tep.txt" , "r" )
s = 0
cho  dòng  trong  tệp :
    s = s + 1
in ( "so dong cua file la:" , s )
tập tin . đóng ()
#cau 7.8
a = input ( 'nhap noi dung danh sach:' )
tệp = mở ( "tep.txt" , "a" )
tập tin . viết ( a )
tập tin . đóng ()
#cau 7.9
tệp = mở ( "tep.txt" , "r" )
a = tập tin . đọc ()
fi = mở ( "abc.txt" , "a" )
fi . viết ( a )
fi . đóng ()
tập tin . đóng ()
#cau 7.10
tệp = mở ( "tep.txt" , "r" )
a = tập tin . đọc ()
b = [ x  với  x  trong  a . chia ( '' )]
c = b [ 0 ]
cho  tôi  trong  b :
    nếu  tôi > c :
        c = tôi
in ( 'chu dai nhat trong van ban la:' , c )
