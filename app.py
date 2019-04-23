import os

from flask import send_from_directory

from mainApp.create import create_app
OS_PATH = os.path.dirname(__file__)


app = create_app()


#下载文件接口
@app.route('/static/<filename>',methods=['GET'])
def get_image(filename):
    # print("get img")
    return send_from_directory(OS_PATH+'/static/',filename)

#下载文件接口
@app.route('/static/<school>/<filename>',methods=['GET'])
def get_portrait(school,filename):
    # print("get img")
    return send_from_directory(OS_PATH+'/static/'+school,filename)

if __name__ == '__main__':
    app.run()
