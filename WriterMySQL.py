from peewee import Model, IntegerField, CharField,DecimalField, MySQLDatabase
import json

# MariaDB의 접속 정보를 config.json로부터 받아온다.
with open('conf/config.json', 'r') as f:
    config = json.load(f)

db = MySQLDatabase(config['MYSQL']['DBNAME'], user=config['MYSQL']['USER'],
                   passwd=config['MYSQL']['PW'], host=config['MYSQL']['HOST'], port=config['MYSQL']['PORT'])



class RepInfoTable(Model):
    rid = IntegerField()
    rep = CharField()
    region = CharField()

    class Meta:
        database = db
        db_table = 'repinfo'
        
class ProductInfoTable(Model):
    pid = IntegerField()
    item = CharField()
    unitCost = DecimalField()
    class Meta:
        database = db
        db_table = 'productinfo'

class SalesOrdersTable(Model):
    rid = IntegerField()
    pid = IntegerField()
    orderDate = CharField()
    units = IntegerField()
    totalCost = DecimalField()

    class Meta:
        database = db
        db_table = 'salesOrders'