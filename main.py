import test,dao

#データベースからデータ全件取得してコンソールに表示
acc_data=dao.find_all()
for acc in acc_data:
    print(acc)

# データベースに1件追加
# user={"acc_date":12,"amount": 110,"item_code":3}
# dao.insert_one(user)

# user={"item_code":3,"item_name": '光熱費'}
# test.insert_two(user)
