from ftpretty import ftpretty
def upload(filename,user="file_uploader",password="mjHV7znKmGdjxsddHfojKWo4lZfk0dO1",host="ap-southeast-1.sftpcloud.io"):
    f=ftpretty(host,user,password)
    only_file_name=filename.split('/')[-1]
    f.put(filename,'/my_upload/'+only_file_name)
   
   
def download(user="file_uploader",password="mjHV7znKmGdjxsddHfojKWo4lZfk0dO1",host="ap-southeast-1.sftpcloud.io"):
    f=ftpretty(host,user,password)
    #only_file_name=filename.split('/')[-1]
    f.get('/my_upload/hello.txt',"done")
    print(" File Downloaded")