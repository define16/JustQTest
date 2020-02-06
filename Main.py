import pandas as pd
import WriterMySQL
import datetime
from datetime import date

if __name__ == '__main__':
    print("[Start]")
    # 엑셀파일 Read
    df = pd.read_excel('data/SampleData.xlsx', sheet_name='SalesOrders')
    rep_df = df.loc[:, ['Rep', 'Region']] # 구매자의 인적사항
    rep_df = rep_df.drop_duplicates('Rep', keep='first') # 중복으로 저장된 구매자 이름를 제거
    rep_df['rid'] = [rid for rid in range(1, len(rep_df)+1)] # 중복되지 않는 rid을 부여
    
    product_df = df.loc[:,['Item','Unit Cost']] # 판매 물건 목록
    product_df = product_df.drop_duplicates(['Item','Unit Cost'], keep='first') # 가격이 같으면 같은 물건으로 취급
    product_df['pid'] = [pid for pid in range(1, len(product_df)+1)] # 중복되지 않는 pid을 부여
    
    df_tmp = pd.merge(df,rep_df.loc[:, ['Rep', 'rid']], left_on='Rep',right_on='Rep') # 전체 데이터에 rid 값 매핑
    df_tmp = pd.merge(df_tmp,product_df.loc[:, ['Item', 'Unit Cost','pid']], left_on=['Item','Unit Cost'],right_on=['Item','Unit Cost']) # 전체 데이터에 pid 값 매핑
    
    salesOrders_df = df_tmp.loc[:, ['rid','pid','OrderDate','Units','Total']] # 거래 내역
    
    
    WriterMySQL.db.connect()# DB 연결
    print("[RepInfoTable] insert")
    for col in rep_df.values.tolist() :
        repinfo_table = WriterMySQL.RepInfoTable(rid=int(col[2]), rep=col[0], region=col[1])
        repinfo_table.save()
        
    print("[ProductInfoTable] insert")
    for col in product_df.values.tolist() :
        product_table = WriterMySQL.ProductInfoTable(pid=int(col[2]), item=col[0], unitCost=float(col[1]))
        product_table.save()
        
    print("[SalesOrdersTable] insert")
    for col in salesOrders_df.values.tolist() :
        salesOrders_table = WriterMySQL.SalesOrdersTable(rid=int(col[0]), pid=int(col[1]), orderDate=str(col[2]).split(" ")[0], units=int(col[3]), totalCost=float(col[4]))
        salesOrders_table.save()
        
    WriterMySQL.db.close() # DB 연결 해제
    print("[Done]")
