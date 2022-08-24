from urllib import request
goo_url='https://www.appsloveworld.com/wp-content/uploads/2018/10/sample-product.csv'
def download_file(csv_url):
    response=request.urlopen(csv_url)
    csv=response.read()
    csv_str=str(csv)
    line=csv_str.split("\\n")
    dest_url='download.csv'
    fx=open(dest_url,"w")
    for lin in line:
        fx.write(lin+"\n")
        print(lin)
    fx.close()
download_file(goo_url)
