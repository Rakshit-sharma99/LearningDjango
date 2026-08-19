from django.http import HttpResponse


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