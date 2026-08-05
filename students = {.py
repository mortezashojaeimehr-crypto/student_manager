import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
students = {
    1:{"name":"علی","family":"حسینی","burn_date":1376,"mobile_number":"09195476367","sexuallity":"مرد"},
    2:{"name":"فریبا","family":"محمودی","burn_date":1378,"mobile_number":"0910984672","sexuallity":"زن"},
    3:{"name":"ساغر","family":"امیری","burn_date":1379,"mobile_number":"09175370934","sexuallity":"زن"},
    }
for student, information in students.items():
    if information["sexuallity"]=="زن" and information["burn_date"]>=1377:
        print(f"کد دانشجویی:{student}")
        print(f"مشخصات:{information}")