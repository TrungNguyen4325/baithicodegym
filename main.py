import csv
import os
from datetime import datetime

FILE_NAME = r"D:\bai\bai_tap_cuoi_khoa\expenses.csv" # CSV nằm cùng thư mục với main.py

# Khởi tạo file CSV nếu chưa có
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])

# Hàm thêm chi tiêu
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Nhập danh mục (ăn uống, đi lại, mua sắm...): ").strip()
    try:
        amount = float(input("Nhập số tiền: ").strip())
    except ValueError:
        print("❌ Số tiền không hợp lệ!")
        return
    note = input("Ghi chú (nếu có): ").strip()

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])
    print("✅ Đã lưu chi tiêu!")

# Hàm xem danh sách chi tiêu
def view_expenses():
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("📂 Chưa có dữ liệu chi tiêu.")
        return

    print("\n--- Danh sách chi tiêu ---")
    for i, row in enumerate(rows, start=1):
        print(f"{i}. Ngày: {row['date']}, Danh mục: {row['category']}, "
              f"Số tiền: {row['amount']}, Ghi chú: {row['note']}")

# Hàm tính tổng chi tiêu
def total_expenses():
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    total = sum(float(row["amount"]) for row in rows)
    print(f"💰 Tổng chi tiêu: {total:,.0f} VND")

# Hàm thống kê theo danh mục
def summary_by_category():
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("📂 Chưa có dữ liệu để thống kê.")
        return

    summary = {}
    for row in rows:
        category = row["category"]
        amount = float(row["amount"])
        summary[category] = summary.get(category, 0) + amount

    print("\n📊 Thống kê chi tiêu theo danh mục:")
    for category, total in summary.items():
        print(f"- {category}: {total:,.0f} VND")

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

        choice = input("Chọn (1-5): ").strip()
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