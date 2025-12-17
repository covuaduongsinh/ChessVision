# Hướng Dẫn Chạy ChessVision (Quick Start Guide)

## Giới Thiệu
ChessVision là một dự án sử dụng computer vision để trích xuất vị trí quân cờ từ hình ảnh bàn cờ.

## Yêu Cầu Hệ Thống
- Python 3.8 hoặc cao hơn
- Linux hoặc MacOS
- Ít nhất 4GB RAM
- GPU (khuyến nghị cho huấn luyện mô hình)

## Cài Đặt Nhanh

### Bước 1: Cài đặt thư viện Python
```bash
pip3 install -r requirements.txt
```

### Bước 2: Tạo thư mục cần thiết
Script `run.sh` sẽ tự động tạo các thư mục cần thiết.

### Bước 3: Chuẩn bị model weights
⚠️ **QUAN TRỌNG**: Ứng dụng cần file model weights để hoạt động.

Bạn cần đặt các file sau vào thư mục `weights/`:
- `best_classifier.hdf5` - Model phân loại quân cờ
- `best_extractor.hdf5` - Model trích xuất bàn cờ

**Lựa chọn để có model weights:**
1. **Huấn luyện mô hình mới** (khuyến nghị nếu có GPU và dữ liệu):
   - Xem hướng dẫn trong `chessvision/training/`
   - Cần có dữ liệu huấn luyện trong `data/`
   
2. **Download weights đã huấn luyện** (nếu có):
   - Liên hệ với người duy trì repository
   - Hoặc kiểm tra trong releases/issues của project gốc

3. **Sử dụng ChessVision-3LC** (phiên bản mới hơn):
   - Project đã chuyển sang: https://github.com/gudbrandtandberg/ChessVision-3LC

## Chạy Ứng Dụng

### Cách 1: Sử dụng script tự động
```bash
./run.sh
```

Script sẽ:
- Kiểm tra và tạo thư mục cần thiết
- Kiểm tra dependencies
- Hướng dẫn khởi động ứng dụng

### Cách 2: Khởi động thủ công

**Terminal 1 - Compute Server:**
```bash
export CVROOT="/home/runner/work/ChessVision/ChessVision"
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/model/
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/data_processing/
export PYTHONPATH=$PYTHONPATH:$CVROOT/chessvision/training/
cd computeroot
python3 cv_endpoint.py --local
```

**Terminal 2 - Web Server:**
```bash
cd webroot
python3 main.py --local server
```

### Truy cập ứng dụng
Sau khi cả hai server đã chạy:
- Web interface: http://localhost:5000
- Compute API: http://localhost:7777

## Sử Dụng

1. Mở trình duyệt và truy cập http://localhost:5000
2. Upload hình ảnh bàn cờ (ít nhất 512x512 pixels, định dạng vuông)
3. Chờ hệ thống xử lý và trích xuất vị trí FEN
4. Xem kết quả và điều chỉnh nếu cần

## Yêu Cầu Hình Ảnh

Để có kết quả tốt nhất, hình ảnh cần:
- Kích thước: ít nhất 512x512 pixels
- Định dạng: vuông (tỷ lệ 1:1)
- Chứa đúng một bàn cờ
- Bàn cờ chiếm ít nhất 35% diện tích ảnh
- Ánh sáng tốt, không bị mờ quá nhiều

## Xử Lý Sự Cố

### Lỗi: Model weights không tìm thấy
```
ERROR: Model weights not found!
```
**Giải pháp**: Bạn cần có file weights. Xem "Bước 3: Chuẩn bị model weights" ở trên.

### Lỗi: Port đã được sử dụng
```
Address already in use
```
**Giải pháp**: 
- Dừng các tiến trình đang sử dụng port 5000 hoặc 7777
- Hoặc thay đổi port trong code

### Lỗi: Import modules thất bại
```
ModuleNotFoundError: No module named 'cv2'
```
**Giải pháp**: Cài đặt lại dependencies
```bash
pip3 install -r requirements.txt
```

### Lỗi: CVROOT environment variable
```
Error related to CVROOT
```
**Giải pháp**: Đảm bảo bạn đã set environment variables đúng cách (xem Cách 2 ở trên)

## Cấu Trúc Thư Mục

```
ChessVision/
├── chessvision/          # Core library code
├── computeroot/          # Compute server (CV algorithm)
│   ├── cv_endpoint.py   # API endpoint
│   ├── user_uploads/    # User uploaded files
│   └── tmp/             # Temporary files
├── webroot/              # Web frontend
│   ├── main.py          # Web server
│   ├── templates/       # HTML templates
│   └── static/          # CSS, JS files
├── weights/              # Model weights (cần tự thêm)
│   ├── best_classifier.hdf5
│   └── best_extractor.hdf5
├── data/                 # Training data
├── requirements.txt      # Python dependencies
└── run.sh               # Startup script
```

## Ghi Chú Bổ Sung

- Project gốc đã chuyển sang ChessVision-3LC (link ở trên)
- Phiên bản này dùng TensorFlow 2.x
- Demo online đôi khi có tại: http://chessvision.net (không đảm bảo luôn hoạt động)

## Hỗ Trợ

- Repository gốc: https://github.com/gudbrandtandberg/ChessVision
- Project mới: https://github.com/gudbrandtandberg/ChessVision-3LC
- Issues: https://github.com/covuaduongsinh/ChessVision/issues

---

**Chúc bạn sử dụng thành công! 🎉**
