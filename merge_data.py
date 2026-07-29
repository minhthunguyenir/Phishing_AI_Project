import pandas as pd

def merge_and_balance_data():
    try:
        print("Đang đọc 2 tập dữ liệu...")
        # Đọc 2 file CSV (Đảm bảo tên file khớp với máy bạn)
        df_benign = pd.read_csv("tranco_top_50k_benign.csv")
        df_phish = pd.read_csv("financial_phishing_urls.csv")
        
        # 1. Cân bằng dữ liệu (Tỷ lệ 1:1)
        n_samples = len(df_phish) # Bằng 15.349
        print(f"Đang lấy mẫu ngẫu nhiên {n_samples} link sạch để cân bằng...")
        df_benign_sampled = df_benign.sample(n=n_samples, random_state=42)
        
        # 2. Gộp 2 bảng lại với nhau
        df_final = pd.concat([df_benign_sampled, df_phish], ignore_index=True)
        
        # 3. Xáo trộn dữ liệu (Shuffle) 
        # Rất quan trọng: Giúp thuật toán không học theo kiểu "thuộc lòng" 
        # nửa đầu là web sạch, nửa sau là web lừa đảo.
        print("Đang xáo trộn dữ liệu (Shuffle)...")
        df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)
        
        # 4. Lưu ra file CSV "trùm cuối"
        output_file = "final_phishing_dataset.csv"
        df_final.to_csv(output_file, index=False)
        
        print(f"\n🎉 HOÀN TẤT TUẦN 1! Đã gộp thành công vào file: {output_file}")
        print(f"Tổng số dòng Dataset: {len(df_final)} (Gồm {n_samples} Sạch và {n_samples} Lừa đảo)")
        print("Xem trước 5 dòng ngẫu nhiên:")
        print(df_final.head())
        
    except FileNotFoundError as e:
        print(f"Lỗi: Không tìm thấy file. Bạn kiểm tra lại tên file nhé! Chi tiết: {e}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    merge_and_balance_data()