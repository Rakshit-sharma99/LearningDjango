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
    return render(request, 'test.html', {'name': 'Rakshit'})






def testimage(request):
    return render(request, 'testimage.html')





def events(request):
    events_list = [
        {'name': 'Event 1', 'date': '2027-01-15', 'image': '/img1.png'},
        {'name': 'Event 2', 'date': '2027-02-20', 'image': '/img2.png'},
        {'name': 'Event 3', 'date': '2027-03-10', 'image': '/img3.png'},
    ]
    return render(request, 'events.html', {'events': events_list})
# ==========================================



# Sabhi events ko booking page par list karne ke liye view
def eventbooking(request):
    events_list = [
        {'name': 'Event 1', 'date': '2027-01-15', 'image': '/img1.png'},
        {'name': 'Event 2', 'date': '2027-02-20', 'image': '/img2.png'},
        {'name': 'Event 3', 'date': '2027-03-10', 'image': '/img3.png'},
    ]
    return render(request, 'booking.html', {'events': events_list})



# def fooddata(request):


# URL se aane wala event name (eventdetails) ke according details render karne ke liye view
def eventbook(request, eventdetails):
    events_list = [
        {'name': 'Event 1', 'date': '2027-01-15', 'image': '/img1.png'},
        {'name': 'Event 2', 'date': '2027-02-20', 'image': '/img2.png'},
        {'name': 'Event 3', 'date': '2027-03-10', 'image': '/img3.png'},
    ]
    # 'events': saari list, aur 'eventdetails': URL se aayi value (jaise 'Event 1')
    return render(request, 'eventdetails.html', {'events': events_list, 'eventdetails': eventdetails})
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

def temp(request):
    return render(request, 'header.html')

def food(request, food_value=None):
    newmenu=[
        {'name':'Pizza','price':250 , 'size':'Large','image': '/img2.png'},
        {'name':'Burger','price':120, 'size':'Medium','image': '/img3.png'},
        {'name':'Ice Cream','price':'Free', 'size':'Small','image': '/img1.png'}
    ]
    return render(request, 'food.html', {'menu': newmenu, 'food_value': food_value})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dob(request, dob):
    return HttpResponse(f"<h2>Date of Birth: {dob}</h2>")


def menu(request, category, subcat=""):
    return HttpResponse(f"<h2>You have chosen category: {category} | You have chosen sub cat: {subcat}</h2>")

def csstest(request):
    return render(request, 'testcss.html')


def plan(request,plan=None):
    plans=[
        {'name': 'plan1'},
        {'name': 'plan2'},
        {'name': 'plan3'}
    ]
    return render(request, 'plans.html', {'plans': plans})

def plan_details(request, plan_name):
    return HttpResponse(f"<h2>Plan Details for: {plan_name}</h2>")



def phones(request,):
    phones =[
        {'name':'samsung'},
        {'name':'apple'}
    ]

    return render(request,'phone.html', {'phones':phones})

def umar(request    ):
    umars =[
        {'age': 20},
        {'age': 25}
    ]
    return render(request, 'umar.html', {'umars': umars})

def home (request):
    return render(request, 'home/home.html')

def base (request):
    return render(request, 'home/base.html')

def about (request):
    return render(request, 'home/about.html')

# def greet(request,name):
#     return HttpResponse(f"Hello {name} good morning")


def dishes(request, food):
    items ={
        'pizza':'Pizza is 150',
        'burger':'burger is 150',
        'chowmin':'chowmin is 150',
    }
    return  HttpResponse(f"<h2>{food}</h2>")


def calc(request):
    val1 = request.GET.get('val1')
    val2 = request.GET.get('val2')
    val3 = request.GET.get('oper')
    if val3 =="add":
        result = int(val1)+int (val2)
    return HttpResponse(f"{result}")

def greet(request, name ,time):
 
    return render(request, 'home/greeting.html',{
        'name':name,
        'time':time
    })


def departments(request):
    depart= [
       { 'name':'cse'},
       { 'name':'bsc'},
       { 'name':'mca'},
       { 'name':'agriculture'},
       { 'name':'law'}
    ]
    return render(request,'college.html', {'depart': depart})

def department_details(request, department_name):
   
    depart = [
        'cse',
        'bsc',
        'mca',
        'agriculture',
        'law'
    ]
    if department_name in depart:
       message = f"you selected: {department_name}"
    else: 
        message =f"Department not available"

    return render(request, 'dep_dtl.html', {'message':message}) 
           
















def student_result(request):
    details=[

      {  'name':'rakshit','course':'django', 'rno':1,'m1':67,'m2':78,'m3':89},
 {       'name':'aman','course':'django', 'rno':2,'m1':67,'m2':78,'m3':89},
        {'name':'akash','course':'django', 'rno':3,'m1':67,'m2':78,'m3':89}
    
    ]
    return render(request, 'stdname.html',{'details':details})






def stdeatils(request, rno):

    details = [
        {'name':'rakshit','course':'django','rno':1,'m1':67,'m2':78,'m3':89},
        {'name':'aman','course':'django','rno':2,'m1':10,'m2':11,'m3':12},
        {'name':'akash','course':'django','rno':3,'m1':67,'m2':78,'m3':89}
    ]

    for std in details:

        if rno == std['rno']:

            m1 = std['m1']
            m2 = std['m2']
            m3 = std['m3']

            total = int(m1) + int(m2) + int(m3)
            average = total / 3

            content = f"{std['name']}, {std['course']}, {std['rno']}, {m1}, {m2}, {m3}"

            return render(request, 'stdetails.html', {'content': content,'average': average })
        content = "student not found"

    return render(request, 'stdetails.html', {'content': content})








def student(request): 
 
    details = [
        {'name1':'raj','course':'django'},
        {'name2':'rohit','course':'django'},
        {'name3':'birju','course':'java'}
    ]
 
    course = request.GET.get('course') 
 
    if course=="django":
        return HttpResponse(f"{{name1}}")
    elif course=="django":
        return HttpResponse(f"{{name2}}")
    elif course=="java":
        return HttpResponse(f"{{name3}}")
    else:
        return HttpResponse(f"{{name1}},{{name2}},{{name3}}")




def htmlform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')                       
        password = request.POST.get('password')
        if name and email and password:
         return HttpResponse(f"<h2>Name:  {name}</h2><h2>Email: {email}</h2><h2>Pass: {password}</h2>")
        else:
            return HttpResponse("<h2>Error: Please fill in all fields.</h2>")
    else:
        return render(request, 'htmlforms.html')