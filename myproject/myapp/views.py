from django.http import HttpResponse
from django.shortcuts import render


# ==========================================
# Custom Error Handlers (500 & 404)
# ==========================================

def custom_500(request):
    return HttpResponse("<h1 style='color: red;'>500 - Internal Server Error</h1>", status=500)


def custom_404(request, exception=None):
    return HttpResponse("<h1>404 - Page Not Found</h1>", status=404)


# ==========================================
# Divide By Zero View (Triggers 500 Error)
# ==========================================

def dv(request):
    # This will trigger a ZeroDivisionError (Server 500 Error)
    result = 10 / 0
    return HttpResponse(f"<h2>Result: {result}</h2>")


# ==========================================
# Templates View
# ==========================================

def mytemplate(request):
    return render(request, 'test.html')


# ==========================================
# Application Views
# ==========================================

def studentdetails(request):
    studentinfo = [
        ["Ram", 67],
        ["Shyam", 89],
        ["Hari", 75]
    ]
    content = """<table>
    <tr>
        <th>Name</th>
        <th>Marks</th>
    </tr>
    """

    for i in studentinfo:
        content += f"""
        <tr>
        <td>{i[0]}</td>
        <td>{i[1]}</td>
        </tr>
        """

    content += "</table>"
    return HttpResponse(content)


def std(request):
    stdd = [
        {"Name": "Rakshit", "Cgpa": 7, "Course": "Cse"},
        {"Name": "Rohit", "Cgpa": 8, "Course": "Cse"},
        {"Name": "Raj", "Cgpa": 9, "Course": "Cse"}
    ]
    content = """<table>
    <tr>
        <th>Name</th>
        <th>Cgpa</th>
        <th>Course</th>
    </tr>
    """

    for i in stdd:
        content += f"""
        <tr>
            <td>{i['Name']}</td>
            <td>{i['Cgpa']}</td>
            <td>{i['Course']}</td>
        </tr>
        """

    content += "</table>"
    return HttpResponse(content)


def std1(request):
    stddd = [
        {"Name": "Rakshit", "Cgpa": 7, "Course": "Cse"},
        {"Name": "Rohit", "Cgpa": 8, "Course": "Cse"},
        {"Name": "Raj", "Cgpa": 9, "Course": "Cse"}
    ]

    content = "<table><tr>"
    # create table headers from the keys
    for key in stddd[0].keys():
        content += f"<th>{key}</th>"
    content += "</tr>"

    # Nested loop to  create r nd c
    for st in stddd:
        content += "<tr>"
        for val in st.values():
            content += f"<td>{val}</td>"
        content += "</tr>"

    content += "</table>"
    return HttpResponse(content)


def std2(request):
    st = {
        "ansh": {"cgpa": 7, "course": "Cse"},
        "rohit": {"cgpa": 8, "course": "Cse"},
        "raj": {"cgpa": 9, "course": "Cse"}
    }
    content = "<table><tr><th>Student</th><th>CGPA</th><th>Course</th></tr>"

    for student, info in st.items():
        content += f"<tr><td>{student}</td>"
        for val in info.values():
            content += f"<td>{val}</td>"
        content += "</tr>"

    content += "</table>"
    return HttpResponse(content)


def fooddie(request, food_value):
    fooditems = {
        "pizza": 250,
        "burger": 120,
        "ice cream": 80
    }

    food = food_value.lower().strip()

    if food in fooditems:
        return HttpResponse(f"<h2>Food: {food_value.title()}</h2><p>Price: Rs. {fooditems[food]}</p>")
    else:
        return HttpResponse(f"<h2>Food: {food_value.title()}</h2><p style='color: red;'>Not Available</p>")


foooddie = fooddie


def mart(request):
    items = request.GET.get('i')
    return HttpResponse(f"<h2>Items: {items}</h2>")


def calculator(request):
    v1 = request.GET.get('v1')
    v2 = request.GET.get('v2')
    try:
        v1 = int(v1)
        v2 = int(v2)
    except (ValueError, TypeError):
        return HttpResponse("<h2>Error: Invalid input values</h2>")

    opr = request.GET.get('opr')

    if opr == 'add':
        result = v1 + v2
    elif opr == 'sub':
        result = v1 - v2
    elif opr == 'mul':
        result = v1 * v2
    elif opr == 'div':
        if v2 == 0:
            return HttpResponse("<h2>Error: Cannot divide by zero in calculator</h2>")
        result = v1 / v2
    else:
        result = "Invalid Operation"

    return HttpResponse(f"<h2>Result: {result}</h2>")


def customer(request, customer_id):
    return HttpResponse(f"<h2>Customer id: {customer_id}</h2>")


def dob(request, dob):
    return HttpResponse(f"<h2>Date of Birth: {dob}</h2>")


def menu(request, category, subcat=""):
    return HttpResponse(f"<h2>You have chosen category: {category} | You have chosen sub cat: {subcat}</h2>")