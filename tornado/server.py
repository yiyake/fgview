# import tornado.ioloop
# import tornado.web
 
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
 
# application = tornado.web.Application([
#     (r"/index", MainHandler),
# ])
 
# if __name__ == "__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()

import tornado.ioloop
import tornado.web
import os.path
import sys
import pymysql
sys.path.append("..")



arr={'yiyake':18 ,'jint':20}
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index01.html")

class AjaxHandler(tornado.web.RequestHandler):
    def post(self):
        g1_id=''
        g2_id=''
        g1info=[]
        g2info=[]
        f1_infos=[]
        f2_infos=[]
        all_data=[]
        all_info={}
        isempty=0
        #self.write("hello world")
        gstr=self.get_argument("message")
        print(self.get_argument("message"))
        g_name=gstr.split('+')
        g1=g_name[0]
        g2=g_name[1]
        print(g1)
        print(g2)
        g1_n=g1
        g2_n=g2
        con=pymysql.connect('127.0.0.1','root','KEyiya19960302','kyy')
        with con:
            cur=con.cursor()
            sql = "SELECT * FROM g_enst \
               WHERE g_name = '%s'" % (g1_n)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:
                if row:
                    row=list(row)
                    print(row)
                    g1_id=row[1]
                    for i in row:
                        g1info.append(i)
                else:
                    isempty=1
                    print("empty")
            #print(g1info)
            print(len(g1info))
            if len(g1info)==0:
                isempty=1
                print("empty")


            sql = "SELECT * FROM g_enst \
               WHERE g_name = '%s'" % (g2_n)
            cur.execute(sql)
            rows=cur.fetchall()
            for row in rows:
                if row:
                    row=list(row)
                    print(row)
                    g2_id=row[1]
                    for i in row:
                       g2info.append(i)
                else:
                    isempty=1
                    print("empty")
            #print(g2info)
            print(len(g2info))
            if len(g2info)==0:
                isempty=1
                print("empty")

            sql2= "SELECT * FROM g_seqs \
               WHERE g_id = '%s'" % (g1_id)
            cur.execute(sql2)
            results=cur.fetchall()
            for line in results:
                if line:
                    line=list(line)
                    g1info.append(line[1])
                    g1info.append(line[2])
                else:
                    isempty=1
                    print("empty")
            print(len(g1info))
            if len(g1info)==0:
                isempty=1
                print("empty")


            g1info.append(0)  
            #print(g1info)
            all_data.append(g1info)

            sql2= "SELECT * FROM g_seqs \
               WHERE g_id = '%s'" % (g2_id)
            cur.execute(sql2)
            results=cur.fetchall()
            for line in results:
                if line:
                    line=list(line)
                    g2info.append(line[1])
                    g2info.append(line[2])
                else:
                    isempty=1
                    print("empty")
            print(len(g2info))
            if len(g2info)==0:
                isempty=1
                print("empty")


            g2info.append(0)    
            #print(g2info)
            all_data.append(g2info)

            sql3= "SELECT * FROM f_info \
               WHERE f_id = '%s'" % (g1_id)
            cur.execute(sql3)
            f1_result=cur.fetchall()
            for line in f1_result:
                if line:
                    line=list(line)
                    f1_infos.append(line)
                    all_data.append(line)
                else:
                    isempty=1
                    print("empty")
            print(len(f1_infos))
            if len(f1_infos)==0:
                isempty=1
                print("empty")
            #all_data.append(f1_infos)

            sql3= "SELECT * FROM f_info \
               WHERE f_id = '%s'" % (g2_id)
            cur.execute(sql3)
            f2_result=cur.fetchall()
            for line in f2_result:
                if line:
                    line=list(line)
                    f2_infos.append(line)
                    all_data.append(line)
                else:
                    isempty=1
                    print("empty")
                
            print(len(f2_infos))
            if len(f2_infos)==0:
                isempty=1
                print("empty")
#all_data.append(f2_infos)
            print(len(all_data))
            k=0
            for i in range(len(all_data)):
                for j in range(len(all_data[0])):
                    all_info[k]=all_data[i][j]
                    k=k+1

            #print(all_info)
        print(isempty)
        print('8888888888888888888888888')          
        con.close()
        if isempty==0:
            self.write(all_info)
        else:
            print("empty")
            self.write('no')



application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/test", AjaxHandler),
    ],
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    )

if __name__ == '__main__':
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()