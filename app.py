from flask import Flask, render_template

app = Flask(__name__)

# 定义根路由(/)的处理函数
@app.route("/")
def home():
    """首页视图函数
    
    返回渲染后的index.html模板作为网站首页内容
    
    Returns:
        str: 渲染后的HTML页面内容
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)