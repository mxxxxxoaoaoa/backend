import psycopg2
import base64

class Database:
    def __init__(self, dbname, user, password):
        self.con = psycopg2.connect("dbname={} user={} password={}".format(dbname, user, password))
        self.cur = self.con.cursor()

    def get_all_posts(self):
        q = 'SELECT * FROM for_sorting;'
        try:
            self.cur.execute(q)
            res = {"results": []}
            for item in self.cur.fetchall():
                files = []
                for i in item[5]:
                    files.append(base64.b64encode(i).decode("utf-8"))
                res['results'].append(
                    {"id": item[0], "group_id": item[1], "group_name": item[2], "post_id": item[3], "timestamp": item[4],
                     "files": files}
                )

            return res
        except Exception as e:
            print(e)
            return {'results': []}

    def get_post(self, id_):
        q = 'SELECT * FROM for_sorting;'
        v = (id_, )
        try:
            self.cur.execute(q, v)
            a = self.cur.fetchone()
            files = []
            for i in a[5]:
                files.append(base64.b64encode(i).decode("utf-8"))
            data = {"id": a[0], "group_id": a[1], "group_name": a[2], "post_id": a[3], "timestamp": a[4],
                     "files": files}
            return data
        except Exception as e:
            print(e)
            return {'message': 'error in db'}
