import test,dao
import pymysql

#データベースからデータ全件取得してコンソールに表示
acc_data=dao.find_all()
for acc in acc_data:
    print(acc)

# データベースに1件追加
user={"acc_date":1202,"amount": 20000,"item_code":1}
dao.insert_one(user)

# user={"item_code":4,"item_name": '税金'}
# test.insert_two(user)

