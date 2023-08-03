from menu_item import MenuItem
import psycopg2
connection = psycopg2.connect(
    database="ExersiceXP_d4", 
    user='postgres',
    password='veampti0312',
    host='localhost',
    port='5432'
)

class MenuManager():
    
    @classmethod
    def get_by_name(cls, item_name):
      try:
            with connection:
                with connection.cursor() as curs:
        

                    query = "SELECT * FROM Menu_Items WHERE item_name = %s"
                    data = (item_name,)

                    curs.execute(query, data)
                    result = curs.fetchone()

                    
                    if result:
                        item_name, item_price = result
                        return MenuItem(item_name, item_price)
                    else:
                        return None
      except Exception as err:
            print(err)

    @classmethod
    def all_items(cls):
       try:
            with connection:
                with connection.cursor() as curs:
        
                    query = "SELECT * FROM Menu_Items"

                    curs.execute(query)
                    results = curs.fetchall()
                    
                    pass
       except Exception as err:
            print(err)

       

       menu_items = []
       for result in results:
                item_name, item_price = result
                menu_items.append(MenuItem(item_name, item_price))

                return menu_items


# connection.close()