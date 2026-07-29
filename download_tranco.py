import pandas as pd
import requests
import zipfile
import io

def download_tranco_data():
    print("Đang kết nối đến Tranco để tải danh sách web sạch...")
    url = "https://tranco-list.eu/top-1m.csv.zip"
    
    try:
        # 1. Tải file zip trực tiếp từ internet
        response = requests.get(url, timeout=30)
        response.raise_for_status() 
        print("Tải thành công! Đang giải nén và lấy 50.000 domain đầu tiên...")
        
        # 2. Giải nén trực tiếp trên RAM (không tạo file rác ra máy)
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            csv_filename = z.namelist()[0]
            # Đọc 50.000 dòng đầu tiên
            df = pd.read_csv(z.open(csv_filename), header=None, names=['rank', 'domain'], nrows=50000)
            
        # 3. Gán nhãn 0 (0 = Web sạch / Benign)
        df['label'] = 0
        df_final = df[['domain', 'label']]
        
        # 4. Lưu ra file CSV chuẩn bị sẵn cho bước gộp
        output_file = "tranco_top_50k_benign.csv"
        df_final.to_csv(output_file, index=False)
        
        print(f"\n🎉 Hoàn tất! Đã lưu file: {output_file}")
        print("Xem trước 5 dòng web sạch đầu tiên:")
        print(df_final.head())
        
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    download_tranco_data()