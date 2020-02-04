import pandas as pd
from JustQ import WriterMySQL

if __name__ == '__main__':
    # 엑셀파일 Read
    seller_df = pd.read_excel('data/SampleData.xlsx', sheet_name='SalesOrders')
    # print (seller_df)

    db = WriterMySQL.Writer() # DB 초기화
    db.connect() # DB 연결
    # DB 테이블에 데이터 삽입

    db.disconnect() # DB 연결 해제