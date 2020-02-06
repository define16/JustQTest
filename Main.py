import pandas as pd
import WriterMySQL

if __name__ == '__main__':
    # 엑셀파일 Read
    df = pd.read_excel('data/SampleData.xlsx', sheet_name='SalesOrders')
    rep_df = df.loc[:, ['Rep', 'Region']] # 구매자의 인적사항
    rep_df = rep_df.drop_duplicates('Rep', keep='first') # 중복으로 저장된 구매자 이름를 제거
    rep_df['id'] = [id for id in range(1, len(rep_df)+1)] # 중복되지 않는 id을 부여
    
    product_df = df.loc[:,['Item','Unit Cost']] # 판매 물건 목록
    product_df = product_df.drop_duplicates(['Item','Unit Cost'], keep='first') # 가격이 같으면 같은 물건으로 취급
    product_df['pid'] = [pid for pid in range(1, len(product_df)+1)] # 중복되지 않는 pid을 부여
    
    df_tmp = pd.merge(df,rep_df.loc[:, ['Rep', 'id']], left_on='Rep',right_on='Rep') # 전체 데이터에 id 값 매핑
    df_tmp = pd.merge(df_tmp,product_df.loc[:, ['Item', 'Unit Cost','pid']], left_on=['Item','Unit Cost'],right_on=['Item','Unit Cost']) # 전체 데이터에 pid 값 매핑
    
    salesOrders_df = df_tmp.loc[:, ['id','pid','OrderDate','Units','Total']] # 거래 내역
    
    print(rep_df)    
    print(product_df)
    print(salesOrders_df)
    
    
    db = WriterMySQL.Writer() # DB 초기화
    db.connect() # DB 연결
    # DB 테이블에 데이터 삽입

    db.disconnect() # DB 연결 해제