from flask import Flask,request,jsonify

from search_data import SearchData

# 创建 flask 应用
app = Flask(__name__)

# 定义路由和处理函数
@app.route('/api/GetNumber', methods=['Get'])
def GetNumber():
    service = SearchData()
    result = service.get_number()
    return str(result)


if __name__ == '__main__':
    app.run(debug=True, host = '192.168.0.45', port = 7002)

