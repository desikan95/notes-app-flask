from app import app


print("Hello from sample_webapp")
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='5000')
