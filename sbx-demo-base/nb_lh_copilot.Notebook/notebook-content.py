# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e5790b3a-a148-4ce0-9230-45f190bd05bd",
# META       "default_lakehouse_name": "lh_bikestore",
# META       "default_lakehouse_workspace_id": "0ee9e1f2-217e-4a54-a920-10ddf8f6b93d",
# META       "known_lakehouses": [
# META         {
# META           "id": "e5790b3a-a148-4ce0-9230-45f190bd05bd"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# <b> Relationships </b>
# 
# dbo.products <br>
# FOREIGN KEY (category_id) REFERENCES categories (category_id) <br>
# FOREIGN KEY (brand_id) REFERENCES brands (brand_id) <br>
# 
# dbo.staffs <br>
# FOREIGN KEY (store_id) REFERENCES stores (store_id) <br>
# 
# dbo.order_items <br>
# FOREIGN KEY (order_id) REFERENCES orders (order_id) <br>
# FOREIGN KEY (product_id) REFERENCES products (product_id) <br>
# 
# dbo.stocks <br>
# FOREIGN KEY (store_id) REFERENCES stores (store_id) <br>
# FOREIGN KEY (product_id) REFERENCES products (product_id) <br>
# 
# dbo.orders <br>
# FOREIGN KEY (store_id) REFERENCES stores (store_id) <br>
# 


# CELL ********************

# MAGIC %%code
# MAGIC return all table names and a count of records


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC load 'dbo.products' into a dataframe called df_products

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC load 'dbo.order_items' into a dataframe called df_orderitems
# MAGIC join df_orderitems to df_products on product_id
# MAGIC select product_name from df_products and list_price and quantity from df_orderitems
# MAGIC group by product_name, sum list_price, sum quantity

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code 
# MAGIC using orders.order_date, create a new column called order_date_formated
# MAGIC order_date is stored as int in the format yyyymmdd, I need order_date_formated to use order_date and cast it to be a date type in yyyy/mm/dd
# MAGIC order_date_formated should be a date format
# MAGIC 
# MAGIC add the order_date_formated column and then update it.

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SELECT * FROM dbo.orders LIMIT 200


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%code
# MAGIC Ask a question!

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
