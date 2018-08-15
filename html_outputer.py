# coding:utf-8

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table style='padding:10px;'>")
        for data in self.datas:
            fout.write("<tr style='padding:10px;'>")
            fout.write("<td style='padding:6px;width:500px;border-top:1px solid #ccc;display:inline-block;word-break:break-all;'>%s</td>" % data['url'])
            fout.write("<td style='padding:6px;width:100px;border-left:1px solid #ccc;border-top:1px solid #ccc' >%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td style='padding:6px;border-left:1px solid #ccc;border-top:1px solid #ccc'>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")