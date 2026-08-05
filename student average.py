import sys
import io
import os
import json
import arabic_reshaper
from bidi.algorithm import get_display

# تنظیمات فارسی و محل ذخیره فایل
sys.stdout = io.TextIOWrapper(sys.stdout.buffer , encoding='utf-8')
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#تابع جدا نشدن حروف فارسی
def farsi_print(text):
    reshaped = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped)
    print(bidi_text)

def farsi_input(prompt):
    farsi_print(prompt)
    return input()

#مدیریت فایل
students = {}
students_file = "students.json"

if os.path.exists("students.json"):
    with open("students.json","r",encoding="utf-8") as f:
        students=json.load(f)

def save_student():
    with open("students.json","w",encoding="utf-8") as f:
        json.dump(students,f,ensure_ascii=False,indent=4)

#تابع کمکی (معدل)
def calculate_average(scores):
    return sum(scores) / len (scores) if scores else 0

#منو
def show_menu():
    farsi_print("\n"+"="*40)
    farsi_print("سیستم مدیریت نمرات دانشجویان")
    farsi_print("="*40)
    farsi_print("عدد گزینه مورد نظر را وارد کنید:")
    farsi_print("1.افزودن دانشجو")
    farsi_print("2.نمایش دانشجویان")
    farsi_print("3.جستجوی دانشجو")
    farsi_print("4.ویرایش نمرات دانشجو")
    farsi_print("5.حذف دانشجو")
    farsi_print("6.نمایش دانشجویان معدل الف")
    farsi_print("7.خروج")
    farsi_print("="*40)

#نمایش مرتب دانشجویان
def show_students_sorted():
    if not students:
        farsi_print("هیچ دانشجویی ثبت نشده است")
        return
    student_list=[]
    for name,scores in students.items():
        avg=calculate_average(scores)
        student_list.append((avg,name,scores))

    student_list.sort(reverse=True)

    farsi_print("\n لیست دانشجویان (به ترتیب معدل)")
    farsi_print("-"*40)
    for avg, name, scores in student_list:
        if avg == 20:
            status = "عالی"
        elif avg >= 17:
            status = "خیلی خوب"
        elif avg >= 15:
            status= "خوب"
        elif avg >= 10:
            status= "متوسط"
        else:
            status= "نیاز به تلاش بیشتر"
        farsi_print(f"{name} : نمرات {scores} - معدل{avg:.2f} - {status}")

#حلقه اصلی
while True:
    show_menu()
    choice = farsi_input("انتخاب کنید")

    if choice == "1":
        name = farsi_input("نام را وارد کنید")
        try:
            math_score = float(farsi_input("نمره ریاضی:"))
            physics_score = float(farsi_input("نمره فیزیک:"))
            chemistry_score = float(farsi_input("نمره شیمی"))
            scores = [math_score, physics_score, chemistry_score]
            students[name] = scores
            save_student()
            farsi_print(f"{name} با نمرات {scores} با موفقیت اضافه شد.")
        except ValueError:
            farsi_print("لطفا عدد وارد کنید")
    
    elif choice == "2":
        show_students_sorted()

    elif choice == "3":
        search = farsi_input("نام دانشجو را وارد کنید")
        found = False
        for name, scores in students.items():
            if search.lower() in name.lower():
                avg= calculate_average(scores)
                farsi_print(f"{name} : نمرات {scores} - معدل{avg:.2f}")
                found = True
        if not found:
            farsi_print("دانشجویی یافت نشد")

    elif choice == "4":
        name = farsi_input("نام دانشجو جهت ویرایش:")
        if name in students:
            try:
                math_score=float(farsi_input("نمره ریاضی:"))
                physics_score=float(farsi_input("نمره فیزیک"))
                chemistry_score=float(farsi_input("نمره شیمی"))
                scores=[math_score,physics_score,chemistry_score]
                students[name]=scores
                save_student()
                farsi_print(f"نمرات {name} به روز شد.")
                
            except ValueError:
                farsi_print("لطفا عدد وارد کنید")

        else:
            farsi_print("دانشجو یافت نشد")

    elif choice == "5":
        name=farsi_input(":نام دانشجو برای حذف")
        if name in students:
            del students[name]
            save_student()
            farsi_print("دانشجو حذف شد")
        else:
            farsi_print("دانشجو یافت نشد")

    elif choice == "6":
        farsi_print("\nدانش جویان برتر(معدل بالای 17)")
        found=False
        for name,scores in students.items():
            avg = calculate_average(scores)
            if avg >=17:
                farsi_print(f"{name} - معدل:{avg:.2f} - نمرات {scores}")
                found=True
        if not found:
                farsi_print("دانشجویی با معدل بالای 17 موجود نیست")

    elif choice == "7":
        farsi_print("خدانگهدار")
        break
    else:
        farsi_print("لطفا از بین اعداد 1 تا 7 یک گزینه را انتخاب کنید")
