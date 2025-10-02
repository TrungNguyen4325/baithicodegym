import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Tạo file CSV nếu chưa có
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount", "note"])

# Ghi chi tiêu mới
def add_expense():
    date = input("Nhập ngày (YYYY-MM-DD, Enter = hôm nay): ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Danh mục (ăn uống, đi lại, mua sắm...): ")

    try:
        amount = float(input("Số tiền: "))
    except ValueError:
        print("Lỗi: Số tiền phải là số!")
        return

    note = input("Ghi chú: ")

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])

    print("Đã thêm chi tiêu!")

# Xem toàn bộ chi tiêu và xuất ra file README.md
def view_expenses():
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # In ra màn hình
    print(["date", "category", "amount", "note"])
    for row in rows:
        print([row["date"], row["category"], row["amount"], row["note"]])

    # Xuất ra file README.md
    md_file = "README.md"
    with open(md_file, mode="w", encoding="utf-8") as f:
        f.write("# 📒 Sổ tay Tài chính Cá nhân\n\n")
        f.write("| Date | Category | Amount | Note |\n")
        f.write("|------|----------|--------|------|\n")
        for row in rows:
            f.write(f"| {row['date']} | {row['category']} | {row['amount']} | {row['note']} |\n")

    print(f"✅ Đã xuất dữ liệu sang {md_file}")

# Tính tổng chi tiêu
def total_expenses():
    total = 0
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["amount"])
    print(f" Tổng chi tiêu: {total:.0f} VND")

# Thống kê theo danh mục
def summary_by_category():
    stats = {}
    with open(FILE_NAME, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cat = row["category"]
            stats[cat] = stats.get(cat, 0) + float(row["amount"])

    print(" Thống kê chi tiêu theo danh mục:")
    for cat, total in stats.items():
        print(f" - {cat}: {total:.0f} VND")

# Menu
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
            print(" Tạm biệt!")
            break
        else:
            print(" Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()