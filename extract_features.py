import pandas as pd
import re

def extract_lexical_features():
    input_file = "final_phishing_dataset.csv"
    output_file = "features_matrix.csv"
    
    try:
        print("Đang đọc tập dữ liệu...")
        df = pd.read_csv(input_file)
        
        print("Đang bóc tách các đặc trưng cấu trúc URL...")
        
        # 1. Chiều dài URL
        df['url_length'] = df['domain'].apply(lambda x: len(str(x)))
        
        # 2. Đếm số lượng dấu chấm
        df['dot_count'] = df['domain'].apply(lambda x: str(x).count('.'))
        
        # 3. Đếm số lượng dấu gạch ngang
        df['hyphen_count'] = df['domain'].apply(lambda x: str(x).count('-'))
        
        # 4. Đếm số lượng ký tự '@'
        df['at_count'] = df['domain'].apply(lambda x: str(x).count('@'))
        
        # 5. Đếm số lượng chữ số
        df['digit_count'] = df['domain'].apply(lambda x: sum(c.isdigit() for c in str(x)))
        
        # 6. Đếm các ký tự đặc biệt khác
        special_chars = re.compile(r'[\?\=\_\&\%\/\|]')
        df['special_char_count'] = df['domain'].apply(lambda x: len(special_chars.findall(str(x))))
        
        # 7. Quét từ khóa tài chính mạo danh
        financial_keywords = [
            'bank', 'vcb', 'techcom', 'paypal', 'forex', 'crypto', 
            'wallet', 'momo', 'vnpay', 'binance', 'login', 'account', 'verify'
        ]
        def has_keyword(url):
            url_lower = str(url).lower()
            return 1 if any(kw in url_lower for kw in financial_keywords) else 0
            
        df['has_financial_keyword'] = df['domain'].apply(has_keyword)
        
        # --- CHÚ Ý: Huỳnh sẽ code phần Entropy (số 8) ở ngay vị trí này ---
        
        
        # Sắp xếp lại cột: Để cột 'label' ở cuối cùng cho chuẩn form Machine Learning
        cols = [c for c in df.columns if c != 'label'] + ['label']
        df = df[cols]
        
        # Lưu ra file ma trận
        df.to_csv(output_file, index=False)
        
        print(f"\n🎉 Xong! Đã trích xuất thành công ma trận đặc trưng vào file: {output_file}")
        print("Xem trước 5 dòng đầu tiên:")
        print(df.head())
        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_file}. Bạn kiểm tra lại nhé.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    extract_lexical_features()