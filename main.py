import sqlite3
import os

DB_NAME = "shogun_ramen.db"

def init_db():
    """เช็กและสร้างฐานข้อมูลจาก schema.sql หากยังไม่มีไฟล์ db"""
    if not os.path.exists(DB_NAME):
        print("Creating database schema...")
        conn = sqlite3.connect(DB_NAME)
        with open("schema.sql", "r", encoding="utf-8") as f:
            schema_script = f.read()
        conn.executescript(schema_script)
        conn.commit()
        conn.close()
        print("Database initialized successfully!")

def main_menu():
    """หน้าจอเมนูหลักของระบบ JAPK Shogun Ramen"""
    init_db()
    while True:
        print("\n==================================")
        print(" JAPK Shogun Ramen & Izakaya System")
        print("==================================")
        print("1. Data Generator (ฝ่ายสุ่มข้อมูล)")
        print("2. Kitchen Display System (ฝ่ายห้องครัว)")
        print("3. Billing & Reports (ฝ่ายคิดเงิน/ออกใบเสร็จ)")
        print("0. Exit (ออกจากโปรแกรม)")
        print("==================================")
        
        choice = input("Select an option (0-3): ").strip()
        
        if choice == '1':
            print("\n[Connecting to Data Generator...]")
            # เดี๋ยวเชื่อมกับงานเพื่อนคนที่ 1
        elif choice == '2':
            print("\n[Connecting to Kitchen System...]")
            # เดี๋ยวเชื่อมกับงานเพื่อนคนที่ 2
        elif choice == '3':
            print("\n[Connecting to Billing System...]")
            # เดี๋ยวเชื่อมกับงานเพื่อนคนที่ 3
        elif choice == '0':
            print("\nThank you! Closing system...")
            break
        else:
            print("\nInvalid option, please try again.")

if __name__ == "__main__":
    main_menu()
