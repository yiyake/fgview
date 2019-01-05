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
        self.render("outindex.html")
        


class KdinfoHandler(tornado.web.RequestHandler):
    def post(self):
        mykdinfo={}
        kdallinfo=[]
        name_1=''
        name_2=''
        count_bp1=0;
        count_bp2=0;
        bp1=''
        bp2=''
        dis1=''
        dis2=''
        c=self.get_argument("message")
        codes=c.split('+')

        name_1=codes[0]
        name_2=codes[1]
        #print("Debug:")
        print("kdinfo print:")
        print(self.get_argument("message"))
        con=pymysql.connect('127.0.0.1','root','KEyiya19960302','kyy')
        with con:
            cur=con.cursor()
            sql = "SELECT * FROM knownbp \
               WHERE gene = '%s'" % (name_1)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:

                if row:
                    count_bp1=count_bp1+1;
                    row=list(row)
                    # kdallinfo.append(row[2])
                    bp1=bp1+row[2]
                    bp1=bp1+','
                    # print(row[2])
                else:
                   # isempty=1
                    print("empty")

            kdallinfo.append(bp1)
              
            sql = "SELECT * FROM knownbp \
               WHERE gene = '%s'" % (name_2)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:

                if row:
                    # count_bp2=count_bp2+1;
                    row=list(row)
                    # kdallinfo.append(row[2])
                    bp2=bp2+row[2]
                    bp2=bp2+','
                    # print(row[2])
                else:
                   # isempty=1
                    print("empty")  
            kdallinfo.append(bp2)

             
            sql = "SELECT * FROM disease \
               WHERE gene = '%s'" % (name_1)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:

                if row:
                    # count_bp2=count_bp2+1;
                    row=list(row)
                    # kdallinfo.append(row[2])
                    dis1=dis1+row[1]
                    dis1=dis1+','
                    # print(row[2])
                else:
                   # isempty=1
                    print("empty")  
            kdallinfo.append(dis1)
            
            sql = "SELECT * FROM disease \
               WHERE gene = '%s'" % (name_2)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:

                if row:
                    count_bp2=count_bp2+1;
                    row=list(row)
                    # kdallinfo.append(row[2])
                    dis2=dis2+row[1]
                    dis2=dis2+','
                    # print(row[2])
                else:
                   # isempty=1
                    print("empty")  
            kdallinfo.append(dis2)
            kdallinfo.append(count_bp1)
            kdallinfo.append(count_bp2)
            k=0
            for i in range(len(kdallinfo)):
                mykdinfo[k]=kdallinfo[i]
                k=k+1

        self.write(mykdinfo)


class FeatureHandler(tornado.web.RequestHandler):
    def post(self):
        code_1=''
        code_2=''
        name_1=''
        name_2=''
        dr1_info=[]
        dr2_info=[]
        dr_all=[]
        codeempty=0
        dr_info={}
        count_1=0
        count_2=0
        c=self.get_argument("message")
        #print("Debug:")
        print(self.get_argument("message"))
        #back='aaaa'
        codes=c.split('+')

        name_1=codes[0]
        name_2=codes[1]
        enstg_1=[]
        enstg_2=[]
        con=pymysql.connect('127.0.0.1','root','KEyiya19960302','kyy')
        with con:
            cur=con.cursor()
            sql = "SELECT * FROM g_enst \
               WHERE g_name = '%s'" % (name_1)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:
                if row:
                    row=list(row)
                   # print(row)
                   # g1_id=row[1]
                    for i in row:
                        enstg_1.append(i)
                else:
                   # isempty=1
                    print("empty")
            code_1=enstg_1[2]

            sql = "SELECT * FROM g_enst \
               WHERE g_name = '%s'" % (name_2)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:
                if row:
                    row=list(row)
                   # print(row)
                   # g1_id=row[1]
                    for i in row:
                        enstg_2.append(i)
                else:
                   # isempty=1
                    print("empty")
            code_2=enstg_2[2]



            sql = "SELECT * FROM gencode \
               WHERE enst = '%s'" % (code_1)
            cur.execute(sql)
            rows=cur.fetchall()
            dr_all
            for row in rows:
                if row:
                    row=list(row)
                    # print(row)
                    for i in row:
                        dr1_info.append(i)
                        dr_all.append(i)
                else:
                    codeempty=1
                    print("empty")
            # print(dr1_info)

            #print(len(g1info))
            if len(dr1_info)==0:
                codeempty=1
                print("empty")
            
            sql = "SELECT * FROM gencode \
               WHERE enst = '%s'" % (code_2)
            cur.execute(sql)
            rows=cur.fetchall()

            for row in rows:
                if row:
                    row=list(row)
                    # print(row)
                    for i in row:
                        dr2_info.append(i)
                        dr_all.append(i)
                else:
                    codeempty=1
                    print("empty")
            # print(dr2_info)
            sql = "SELECT * FROM mir \
               WHERE gene = '%s'" % (name_1)
            cur.execute(sql)
            row=cur.fetchone()
            if row:
                row=list(row)
                 # print(row)
                for i in row:
                    dr_all.append(i)
            else:
                dr_all.append('0')
                dr_all.append('0')
                dr_all.append('0')


            sql = "SELECT * FROM mir \
               WHERE gene = '%s'" % (name_2)
            cur.execute(sql)
            row=cur.fetchone()
            if row:
                row=list(row)
                # print(row)
                for i in row:
                    dr_all.append(i)

            else:
                dr_all.append('0')
                dr_all.append('0')
                dr_all.append('0')



            sql = "SELECT * FROM tf \
               WHERE gene = '%s'" % (name_1)
            cur.execute(sql)
            rows=cur.fetchall()
            if rows:
                for row in rows:
                    if row:
                        row=list(row)
                        # print(row)
                        for i in row:
                            dr_all.append(i)
            else:
                dr_all.append('0')
                dr_all.append('0')

            sql = "SELECT * FROM tf \
               WHERE gene = '%s'" % (name_2)
            cur.execute(sql)
            rows=cur.fetchall()
            if rows:
                for row in rows:
                    if row:
                        row=list(row)
                        # print(row)
                        for i in row:
                            dr_all.append(i)
            else:
                dr_all.append('0')
                dr_all.append('0')

            sql = "SELECT * FROM mrnaseq \
               WHERE enst = '%s'" % (code_1)
            cur.execute(sql)
            rows=cur.fetchall()
            if rows:
                for row in rows:
                    if row:
                        row=list(row)
                        # print(row)
                        for i in row:
                            dr_all.append(i)
            else:
                dr_all.append('0')
                dr_all.append('0')
                dr_all.append('0')

            sql = "SELECT * FROM mrnaseq \
               WHERE enst = '%s'" % (code_2)
            cur.execute(sql)
            rows=cur.fetchall()
            if rows:
                for row in rows:
                    if row:
                        row=list(row)
                        # print(row)
                        for i in row:
                            dr_all.append(i)
            else:
                dr_all.append('0')
                dr_all.append('0')
                dr_all.append('0')

            sql = "SELECT * FROM variant \
               WHERE name = '%s'" % (name_1)
            cur.execute(sql)
            rows=cur.fetchall()
            if rows:
                for row in rows:
                    if row:
                        row=list(row)
                        # print(row)
                        for i in row:
                            dr_all.append(i)
                    count_1=count_1+1
            else:
                count_1=0


            sql = "SELECT * FROM variant \
               WHERE name = '%s'" % (name_2)
            cur.execute(sql)
            rows=cur.fetchall()
            if rows:
                for row in rows:
                    if row:
                        row=list(row)
                        # print(row)
                        for i in row:
                            dr_all.append(i)
                    count_2=count_2+1
            else:
                count_2=0

            dr_all.append(count_1)
            dr_all.append(count_2)
            #print(len(g1info))
            if len(dr2_info)==0:
                codeempty=1
                # print("empty")
            k=0
            if codeempty==0:
                print(dr_all)
                for i in range(len(dr_all)):
                    dr_info[k]=dr_all[i]
                    k=k+1
                
        con.close()
        if codeempty==0:
            self.write(dr_info)
        else:
            print("empty")
            self.write('no') 
        # self.write('yes')

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
            if isempty==0:
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
    (r"/myfeature", FeatureHandler),
    (r"/kdinfo", KdinfoHandler),
    ],
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    )

if __name__ == '__main__':
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
    }
    application.listen(80)
    tornado.ioloop.IOLoop.instance().start()