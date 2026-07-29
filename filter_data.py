import pandas as pd

def extract_financial_data():
    input_file = "dataset.csv" 
    
    try:
        print("Đang đọc bộ dữ liệu URL thô...")
        df = pd.read_csv(input_file)
        
        # 1. Cột nhãn tên là 'label' và giá trị lừa đảo là 1
        df_phish = df[df['label'] == 1].copy() 
        
        print(f"Tổng số URL lừa đảo ban đầu: {len(df_phish)}")
        
        # 2. Bộ từ khóa tài chính
        financial_keywords = [
            'bank', 'vcb', 'techcom', 'paypal', 'forex', 'crypto', 
            'wallet', 'momo', 'vnpay', 'binance', 'login', 'account', 'verify'
        ]
        
        def is_financial(url):
            url_lower = str(url).lower()
            return any(kw in url_lower for kw in financial_keywords)
        
        # 3. Lọc giữ lại các link mạo danh tài chính
        print("Đang quét từ khóa tài chính...")
        df_financial = df_phish[df_phish['url'].apply(is_financial)].copy()
        
        print(f"Số URL Phishing Tài chính lọc được: {len(df_financial)}")
        
        # 4. BỎ HẾT các cột người ta tính sẵn, chỉ lấy đúng 'url' và 'label'
        df_final = df_financial[['url', 'label']].rename(columns={'url': 'domain'})
        
        # 5. Lưu ra file CSV mới 
        output_file = "financial_phishing_urls.csv"
        df_final.to_csv(output_file, index=False)
        
        print(f"\n🎉 Xong! Đã tạo thành công file: {output_file}")
        print("Xem trước 5 dòng:")
        print(df_final.head())
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_file}.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    extract_financial_data()