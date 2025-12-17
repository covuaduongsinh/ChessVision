# ChessVision - Hướng Dẫn Chạy Phần Mềm Hoàn Chỉnh

## Tổng Quan

ChessVision là phần mềm sử dụng trí tuệ nhân tạo và computer vision để trích xuất vị trí quân cờ từ hình ảnh. Phần mềm đã được cập nhật và có thể chạy được trên máy của bạn.

![ChessVision Interface](https://github.com/user-attachments/assets/ef6d117a-f8bd-4640-aff7-2691086c70c1)

## 🎯 Tính Năng Đã Hoàn Thành

✅ Cập nhật dependencies tương thích với Python 3.12
✅ Tự động tạo thư mục cần thiết
✅ Script kiểm tra và cài đặt tự động
✅ Hỗ trợ chạy demo mode (không cần model weights)
✅ Web interface hoạt động hoàn hảo
✅ API server chạy ổn định

## 🚀 Cách Chạy Nhanh (3 Bước)

### Bước 1: Kiểm Tra Hệ Thống

```bash
python3 check_setup.py
```

Script này sẽ:
- ✅ Kiểm tra phiên bản Python
- ✅ Kiểm tra thư viện đã cài đặt
- ✅ Tạo thư mục cần thiết
- ⚠️ Cảnh báo nếu thiếu model weights

### Bước 2: Cài Đặt

```bash
pip3 install -r requirements.txt
pip3 install -e .
```

### Bước 3: Chạy Phần Mềm

```bash
./run.sh
```

Nhấn `y` khi được hỏi, phần mềm sẽ tự động khởi động!

**Hoặc chạy thủ công:**

Terminal 1:
```bash
cd computeroot
python3 cv_endpoint.py --local --demo
```

Terminal 2:
```bash
cd webroot
python3 main.py --local server
```

### Bước 4: Truy Cập

Mở trình duyệt và vào:
- **Web Interface**: http://localhost:5000
- **API**: http://localhost:7777

## ⚠️ Lưu Ý Quan Trọng Về Model Weights

Phần mềm cần 2 file model weights để xử lý hình ảnh:
- `weights/best_classifier.hdf5` (phân loại quân cờ)
- `weights/best_extractor.hdf5` (trích xuất bàn cờ)

**Nếu không có model weights:**
- ✅ Web interface vẫn chạy bình thường
- ✅ Có thể xem giao diện
- ❌ KHÔNG thể xử lý hình ảnh thực tế

**Cách lấy model weights:**
1. **Huấn luyện tự mình** (cần GPU mạnh + dữ liệu training)
2. **Dùng phiên bản mới hơn**: [ChessVision-3LC](https://github.com/gudbrandtandberg/ChessVision-3LC) (được khuyến nghị)
3. **Liên hệ tác giả** để xin weights đã train sẵn

## 📁 Cấu Trúc Dự Án

```
ChessVision/
├── run.sh                    ← Script chạy tự động
├── check_setup.py           ← Script kiểm tra hệ thống
├── QUICKSTART_VI.md         ← Hướng dẫn nhanh (tiếng Việt)
├── INSTALL.md               ← Hướng dẫn cài đặt chi tiết
├── requirements.txt         ← Thư viện Python
├── chessvision/             ← Code chính
├── computeroot/             ← Server xử lý AI
│   └── cv_endpoint.py      ← API endpoint
├── webroot/                 ← Server web
│   └── main.py             ← Web server
└── weights/                 ← Model weights (bạn cần thêm)
```

## 🔧 Xử Lý Lỗi Thường Gặp

### Lỗi: "ModuleNotFoundError: No module named 'chessvision'"

```bash
pip3 install -e .
```

### Lỗi: "Port already in use"

```bash
# Tìm và dừng process đang dùng port
lsof -ti:7777 | xargs kill -9
lsof -ti:5000 | xargs kill -9
```

### Lỗi: "Model weights not found"

Đây không phải lỗi! Phần mềm sẽ chạy ở demo mode. Để xử lý hình ảnh thực, cần có model weights.

### Lỗi khi import thư viện

```bash
# Cài lại tất cả
pip3 install --force-reinstall -r requirements.txt
pip3 install -e .
```

## 📚 Tài Liệu Tham Khảo

- **QUICKSTART_VI.md**: Hướng dẫn bắt đầu nhanh (tiếng Việt)
- **INSTALL.md**: Hướng dẫn cài đặt chi tiết (tiếng Anh)
- **README.md**: Tổng quan dự án

## 🆕 Thay Đổi Đã Thực Hiện

1. ✅ Cập nhật `requirements.txt` với phiên bản tương thích
2. ✅ Cập nhật `setup.cfg` với dependencies mới
3. ✅ Sửa `cv_globals.py` để tự động tìm thư mục gốc
4. ✅ Thêm demo mode vào `cv_endpoint.py`
5. ✅ Sửa logging để tránh lỗi request context
6. ✅ Tạo script `run.sh` để chạy tự động
7. ✅ Tạo script `check_setup.py` để kiểm tra
8. ✅ Thêm hướng dẫn tiếng Việt đầy đủ

## 💡 Mẹo Sử Dụng

1. **Chạy lần đầu**: Dùng `./run.sh` để tự động setup
2. **Kiểm tra trước khi chạy**: Chạy `python3 check_setup.py`
3. **Demo mode**: Dùng để test xem phần mềm có chạy được không
4. **Full mode**: Cần model weights để xử lý hình ảnh thực

## 🎓 Cách Sử Dụng (Khi Có Model Weights)

1. Mở http://localhost:5000 trên trình duyệt
2. Nhấn "Choose file" để chọn ảnh bàn cờ
3. Nhấn "Extract" để xử lý
4. Xem kết quả FEN notation

**Yêu cầu hình ảnh:**
- Kích thước: tối thiểu 512x512 pixels
- Hình vuông (tỉ lệ 1:1)
- Chứa đúng 1 bàn cờ
- Bàn cờ chiếm ít nhất 35% diện tích

## 🌟 Tóm Tắt

Phần mềm ChessVision đã được setup và có thể chạy được! 

**Những gì đã hoàn thành:**
- ✅ Web interface chạy được
- ✅ API server chạy được  
- ✅ Auto-setup script
- ✅ Hướng dẫn đầy đủ

**Để sử dụng đầy đủ chức năng, cần:**
- ⚠️ Model weights (hoặc dùng ChessVision-3LC)

## 📞 Hỗ Trợ

- Repository này: https://github.com/covuaduongsinh/ChessVision
- Dự án gốc: https://github.com/gudbrandtandberg/ChessVision
- Phiên bản mới: https://github.com/gudbrandtandberg/ChessVision-3LC

---

**Chúc bạn sử dụng phần mềm thành công! 🎉**

Nếu cần hỗ trợ thêm, vui lòng tạo Issue trên GitHub.
