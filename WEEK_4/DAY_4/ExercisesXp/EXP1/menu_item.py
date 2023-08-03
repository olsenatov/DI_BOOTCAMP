import psycopg2
# CONNECT TO THE DATABASE
connection = psycopg2.connect(
    database="ExersiceXP_d4", 
    user='postgres',
    password='veampti0312',
    host='localhost',
    port='5432'
)

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def save(self):
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""
                    INSERT INTO menu_items (item_name, item_price)
                    Values ('{self.name}', {self.price})
                    """
                    curs.execute(query)
                    connection.commit()
                    # data = curs.fetchall()
                    # print(data)
                pass
       
        except Exception as err:
            print(err)
            

        
    def delete(self):
         try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""
                    DELETE FROM Menu_Items where item_name = '{self.name}'
                    """
                    curs.execute(query)
                    connection.commit()
                    # data = curs.fetchall()
                    # print(data)
                pass
         except Exception as err:
            print(err)
        
    def update(self, new_name = None, new_price = None):
        try:
            with connection:
                with connection.cursor() as curs:
                    if new_name == None:
                        query = f"""
                        UPDATE menu_items SET item_price = {new_price} where item_name = '{self.name}'
                         """
                    elif new_price == None:
                        print("bad")
                        query = f"""
                        UPDATE menu_items SET item_name = '{new_name}' where item_name = '{self.name}' 
                         """ 
                    elif new_name != None and new_price != None:
                        query = f""" UPDATE menu_items SET item_name = '{new_name}', item_price = {new_price} where item_name = '{self.name}'
                        """  
                        print(query)
                    else:
                        print("Invalid. Pick name or price to change, or both")
                        
                    curs.execute(query)
                    connection.commit()
                #     print(data)
                pass
        except Exception as err:
            print(err)
    
    
# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
    
    
    