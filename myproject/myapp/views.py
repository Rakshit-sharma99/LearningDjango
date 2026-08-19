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
