import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv" # CSV nằm cùng thư mục với main.py

# Khởi tạo CSV nếu chưa có
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date","category","amount","note"])

# Gọi init_file trước khi đọc
init_file()
with open(FILE_NAME, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Kiểm tra dữ liệu
for row in rows:
    print(f"Ngày: {row['date']}, Danh mục: {row['category']}, Số tiền: {row['amount']}, Ghi chú: {row['note']}")

# (Các hàm add_expense, view_expenses, total_expenses, summary_by_category giữ nguyên)
# ...
# Menu chính
def menu():
    init_file()
    while True:
        print("\n=== Sổ tay Tài chính Cá nhân ===")
        print("1. Thêm chi tiêu")
        print("2. Xem chi tiêu")
        print("3. Tính tổng chi tiêu")
        print("4. Thống kê theo danh mục")
        print("5. Thoát")

        choice = input("Chọn (1-5): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            summary_by_category()
        elif choice == "5":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()