from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['ind'] == 'Hostel_rooms':
            return redirect ('/hostel_rooms')
        if request.form['ind'] == 'Hostel':
            return redirect ('/hostel')
        if request.form['ind'] == 'Furniture':
            return redirect ('/furniture')
        if request.form['ind'] == 'Staff':
            return redirect ('/staff')
        if request.form['ind'] == 'Staff_works_for':
            return redirect ('/staff_works_for')
        if request.form['ind'] == 'Warden':
            return redirect ('/warden')
        if request.form['ind'] == 'Warden_contact':
            return redirect ('/warden_contact')
        if request.form['ind'] == 'Student':
            return redirect ('/student')
        if request.form['ind'] == 'Postgrad':
            return redirect ('/postgrad')
        if request.form['ind'] == 'Undergrad':
            return redirect ('/undergrad')
        if request.form['ind'] == 'Student_contact':
            return redirect ('/student_contact')
        if request.form['ind'] == 'Leave_rec':
            return redirect ('/leave_rec')
        if request.form['ind'] == 'Transaction':
            return redirect ('/transaction')
        if request.form['ind'] == 'Student_hostel_payment':
            return redirect ('/student_hostel_payment')    
            
    return render_template('index.html')

@app.route('/hostel', methods=['GET', 'POST'])
def hostel():
    if request.method == 'POST':
        if request.form['sub'] == 'Show Table':
            # Fetch form data
            return redirect('/newview')

        if request.form['sub'] == 'Insert':
            # Fetch form data
            hostelDetails = request.form
            block_name = hostelDetails['block_name']
            capacity = hostelDetails['capacity']
            occupancy=hostelDetails['occupancy']
            laundry_days=hostelDetails['laundry_days']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO hostel VALUES(%s, %s, %s, %s)",(block_name, occupancy, capacity, laundry_days))
            mysql.connection.commit()
            cur.close()
        if request.form['sub'] == 'Update':
            hostelDetails = request.form
            block_name = hostelDetails['block_name']
            capacity = hostelDetails['capacity']
            occupancy=hostelDetails['occupancy']
            laundry_days=hostelDetails['laundry_days']
            cur = mysql.connection.cursor()
            cur.execute("update hostel set occupancy=%s, capacity=%s, laundry_days=%s where block_name=%s", (occupancy, capacity, laundry_days, block_name))
            mysql.connection.commit()
            cur.close()
        if request.form['sub'] == 'Delete':
            hostelDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            block_name = hostelDetails['block_name']
            # capacity = hostelDetails['capacity']
            # occupancy=hostelDetails['occupancy']
            # laundry_days=hostelDetails['laundry_days']

            cur = mysql.connection.cursor()
            cur.execute("delete from hostel where block_name = %s", (block_name))
            mysql.connection.commit()
            cur.close()

        return redirect('/newview')
    return render_template('Hostel.html')

@app.route('/newview', methods=['GET', 'POST'])
def new():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM hostel")
    if resultValue > 0:
        hostelDetails = cur.fetchall()
        return render_template('hostelview.html',hostelDetails=hostelDetails)


@app.route('/hostel_rooms', methods=['GET', 'POST'])
def hostel_rooms():
    if request.method == 'POST':
        if request.form['hos'] == 'Show Table':
            # Fetch form data
            return redirect('/hostel_roomsview')

        if request.form['hos'] == 'Insert':
            # Fetch form data
            hostel_roomsDetails = request.form
            block_name = hostel_roomsDetails['block_name']
            room_no = hostel_roomsDetails['room_no']
            sharing_type=hostel_roomsDetails['sharing_type']
            floor=hostel_roomsDetails['floor']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO hostel_rooms VALUES(%s, %s, %s, %s)",(block_name, room_no, sharing_type, floor))
            mysql.connection.commit()
            cur.close()
        if request.form['hos'] == 'Update':
            hostel_roomsDetails = request.form
            block_name = hostel_roomsDetails['block_name']
            room_no = hostel_roomsDetails['room_no']
            sharing_type=hostel_roomsDetails['sharing_type']
            floor=hostel_roomsDetails['floor']
            cur = mysql.connection.cursor()
            cur.execute("update hostel_rooms set block_name=%s, sharing_type=%s, floor=%s where room_no=%s", ( block_name, sharing_type, floor, room_no))
            mysql.connection.commit()
            cur.close()
        if request.form['hos'] == 'Delete':
            hostel_roomsDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            block_name = hostel_roomsDetails['block_name']
            room_no = hostel_roomsDetails['room_no']
            # sharing_type=hostel_roomsDetails['sharing_type']
            # floor=hostel_roomsDetails['floor']
            cur = mysql.connection.cursor()
            cur.execute("delete from hostel_rooms where block_name = %s and room_no = %s", (block_name, room_no))
            mysql.connection.commit()
            cur.close()

        return redirect('/hostel_roomsview')
    return render_template('hostel_rooms.html')

@app.route('/hostel_roomsview', methods=['GET', 'POST'])
def hos():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM hostel_rooms")
    if resultValue > 0:
        hostel_roomsDetails = cur.fetchall()
        return render_template('hostel_roomsview.html',hostel_roomsDetails=hostel_roomsDetails)


@app.route('/warden', methods=['GET', 'POST'])
def warden():
    if request.method == 'POST':
        if request.form['war'] == 'Show Table':
            # Fetch form data
            return redirect('/wardenview')

        if request.form['war'] == 'Insert':
            # Fetch form data
            wardenDetails = request.form
            block_name = wardenDetails['block_name']
            warden_id = wardenDetails['warden_id']
            name=wardenDetails['name']
            salary=wardenDetails['salary']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO warden VALUES(%s, %s, %s, %s)",(warden_id,name,salary,block_name))
            mysql.connection.commit()
            cur.close()
        if request.form['war'] == 'Update':
            wardenDetails = request.form
            block_name = wardenDetails['block_name']
            warden_id = wardenDetails['warden_id']
            name=wardenDetails['name']
            salary=wardenDetails['salary']
            cur = mysql.connection.cursor()
            cur.execute("update warden set block_name=%s, salary=%s, name=%s where warden_id=%s", (block_name,salary,name,warden_id))
            mysql.connection.commit()
            cur.close()
        if request.form['war'] == 'Delete':
            wardenDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            # block_name = wardenDetails['block_name']
            warden_id = wardenDetails['warden_id']
            # name=wardenDetails['name']
            # salary=wardenDetails['salary']
            cur = mysql.connection.cursor()
            cur.execute("delete from warden where warden_id = %s", (warden_id))
            mysql.connection.commit()
            cur.close()

        return redirect('/wardenview')
    return render_template('warden.html')

@app.route('/wardenview', methods=['GET', 'POST'])
def war():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM warden")
    if resultValue > 0:
        wardenDetails = cur.fetchall()
        return render_template('wardenview.html',wardenDetails=wardenDetails)

@app.route('/furniture', methods=['GET', 'POST'])
def furniture():
    if request.method == 'POST':
        if request.form['fur'] == 'Show Table':
            # Fetch form data
            return redirect('/furnitureview')

        if request.form['fur'] == 'Insert':
            # Fetch form data
            furnitureDetails = request.form
            room_no = furnitureDetails['room_no']
            type = furnitureDetails['type']
            price=furnitureDetails['price']
            block_name=furnitureDetails['block_name']
            furniture_id=furnitureDetails['furniture_id']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO FURNITURE VALUES(%s, %s, %s, %s, %s)",(furniture_id, type, price, block_name, room_no))
            mysql.connection.commit()
            cur.close()
        if request.form['fur'] == 'Update':
            furnitureDetails = request.form
            room_no = furnitureDetails['room_no']
            type = furnitureDetails['type']
            price=furnitureDetails['price']
            block_name=furnitureDetails['block_name']
            furniture_id=furnitureDetails['furniture_id']
            cur = mysql.connection.cursor()
            cur.execute("update furniture set block_name=%s, room_no=%s, type=%s, price=%s where furniture_id=%s", (block_name, room_no, type, price, furniture_id))
            mysql.connection.commit()
            cur.close()
        if request.form['fur'] == 'Delete':
            furnitureDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            # room_no = furnitureDetails['room_no']
            # type = furnitureDetails['type']
            # price=furnitureDetails['price']
            # block_name=furnitureDetails['block_name']
            furniture_id=furnitureDetails['furniture_id']
            cur = mysql.connection.cursor()
            cur.execute("delete from furniture where furniture_id = %s", (furniture_id))
            mysql.connection.commit()
            cur.close()

        return redirect('/furnitureview')
    return render_template('furniture.html')

@app.route('/furnitureview', methods=['GET', 'POST'])
def fur():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM furniture")
    if resultValue > 0:
        furnitureDetails = cur.fetchall()
        return render_template('furnitureview.html',furnitureDetails=furnitureDetails)


@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method == 'POST':
        if request.form['stu'] == 'Show Table':
            # Fetch form data
            return redirect('/studentview')

        if request.form['stu'] == 'Insert':
            # Fetch form data
            studentDetails = request.form
            roll_no = studentDetails['roll_no']
            name = studentDetails['name']
            branch=studentDetails['branch']
            street=studentDetails['street']
            city=studentDetails['city']
            state=studentDetails['state']
            DoB=studentDetails['DoB']
            email_id=studentDetails['email_id']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(roll_no, name, branch, street, city, state, DoB, email_id ))
            mysql.connection.commit()
            cur.close()
        if request.form['stu'] == 'Update':
            studentDetails = request.form
            roll_no = studentDetails['roll_no']
            name = studentDetails['name']
            branch=studentDetails['branch']
            street=studentDetails['street']
            city=studentDetails['city']
            state=studentDetails['state']
            DoB=studentDetails['DoB']
            email_id=studentDetails['email_id']
            cur = mysql.connection.cursor()
            cur.execute("update student set name=%s, branch=%s, street=%s, city=%s, state=%s, DoB=%s, email_id=%s where roll_no=%s", (name, branch, street, city, state, DoB, email_id, roll_no))
            mysql.connection.commit()
            cur.close()
        if request.form['stu'] == 'Delete':
            studentDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            roll_no = studentDetails['roll_no']
            # name = studentDetails['name']
            # branch=studentDetails['branch']
            # street=studentDetails['street']
            # city=studentDetails['city']
            # state=studentDetails['state']
            # DoB=studentDetails['DoB']
            # email_id=studentDetails['email_id']
            cur = mysql.connection.cursor()
            cur.execute("delete from student where roll_no = %s", (roll_no))
            mysql.connection.commit()
            cur.close()


        return redirect('/studentview')
    return render_template('student.html')

@app.route('/studentview', methods=['GET', 'POST'])
def stu():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM student")
    if resultValue > 0:
        studentDetails = cur.fetchall()
        return render_template('studentview.html',studentDetails=studentDetails)


@app.route('/warden_contact', methods=['GET', 'POST'])
def warden_contact():
    if request.method == 'POST':
        if request.form['warc'] == 'Show Table':
            # Fetch form data
            return redirect('/warden_cview')

        if request.form['warc'] == 'Insert':
            # Fetch form data
            warden_cDetails = request.form
            warden_id = warden_cDetails['warden_id']
            contact = warden_cDetails['contact']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO warden_contact VALUES(%s, %s)",(warden_id, contact ))
            mysql.connection.commit()
            cur.close()
        if request.form['warc'] == 'Update':
            warden_cDetails = request.form
            warden_id = warden_cDetails['warden_id']
            contact = warden_cDetails['contact']
            cur = mysql.connection.cursor()
            cur.execute("update warden_contact set contact=%s where warden_id=%s", (contact, warden_id))
            mysql.connection.commit()
            cur.close()
        if request.form['warc'] == 'Delete':
            warden_cDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            warden_id = warden_cDetails['warden_id']
            contact = warden_cDetails['contact']
            cur = mysql.connection.cursor()
            cur.execute("delete from warden_c where warden_id= %s and contact= %s", (warden_id, contact))
            mysql.connection.commit()
            cur.close()


        return redirect('/warden_cview')
    return render_template('warden_contact.html')

@app.route('/warden_cview', methods=['GET', 'POST'])
def warc():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM warden_contact")
    if resultValue > 0:
        warden_cDetails = cur.fetchall()
        return render_template('warden_cview.html',warden_cDetails=warden_cDetails)

@app.route('/undergrad', methods=['GET', 'POST'])
def undergrad():
    if request.method == 'POST':
        if request.form['ung'] == 'Show Table':
            # Fetch form data
            return redirect('/undergradview')

        if request.form['ung'] == 'Insert':
            # Fetch form data
            undergradDetails = request.form
            roll_no = undergradDetails['roll_no']
            JEE_score = undergradDetails['JEE_score']
            block_name=undergradDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO undergrad VALUES(%s, %s, %s)",(roll_no, JEE_score, block_name ))
            mysql.connection.commit()
            cur.close()
        if request.form['ung'] == 'Update':
            undergradDetails = request.form
            roll_no = undergradDetails['roll_no']
            JEE_score = undergradDetails['JEE_score']
            block_name=undergradDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("update undergrad set block_name=%s, JEE_score=%s where roll_no=%s", (block_name, JEE_score, roll_no))
            mysql.connection.commit()
            cur.close()
        if request.form['ung'] == 'Delete':
            undergradDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            roll_no = undergradDetails['roll_no']
            # JEE_score = undergradDetails['JEE_score']
            # block_name=undergradDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("delete from undergrad where roll_no = %s", (roll_no))
            mysql.connection.commit()
            cur.close()


        return redirect('/undergradview')
    return render_template('undergrad.html')

@app.route('/undergradview', methods=['GET', 'POST'])
def ung():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM undergrad")
    if resultValue > 0:
        undergradDetails = cur.fetchall()
        return render_template('undergradview.html',undergradDetails=undergradDetails)

@app.route('/postgrad', methods=['GET', 'POST'])
def postgrad():
    if request.method == 'POST':
        if request.form['psg'] == 'Show Table':
            # Fetch form data
            return redirect('/postgradview')

        if request.form['psg'] == 'Insert':
            # Fetch form data
            postgradDetails = request.form
            roll_no = postgradDetails['roll_no']
            supervisor = postgradDetails['supervisor']
            block_name=postgradDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO postgrad VALUES(%s, %s, %s)",(roll_no, supervisor, block_name ))
            mysql.connection.commit()
            cur.close()
        if request.form['psg'] == 'Update':
            postgradDetails = request.form
            roll_no = postgradDetails['roll_no']
            supervisor = postgradDetails['supervisor']
            block_name=postgradDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("update postgrad set block_name=%s, supervisior=%s where roll_no=%s", (block_name, supervisor, roll_no))
            mysql.connection.commit()
            cur.close()
        if request.form['psg'] == 'Delete':
            postgradDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            roll_no = postgradDetails['roll_no']
            # supervisor = postgradDetails['supervisor']
            # block_name=postgradDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("delete from postgrad where roll_no = %s", (roll_no))
            mysql.connection.commit()
            cur.close()
        return redirect('/postgradview')
    return render_template('postgrad.html')

@app.route('/postgradview', methods=['GET', 'POST'])
def psg():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM postgrad")
    if resultValue > 0:
        postgradDetails = cur.fetchall()
        return render_template('postgradview.html',postgradDetails=postgradDetails)

@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    if request.method == 'POST':
        if request.form['trans'] == 'Show Table':
            # Fetch form data
            return redirect('/transactionview')

        if request.form['trans'] == 'Insert':
            # Fetch form data
            transactionDetails = request.form
            transaction_id = transactionDetails['transaction_id']
            amount = transactionDetails['amount']
            mode_of_payment=transactionDetails['mode_of_payment']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO transaction VALUES(%s, %s, %s)",(transaction_id, amount, mode_of_payment ))
            mysql.connection.commit()
            cur.close()
        if request.form['trans'] == 'Update':
            transactionDetails = request.form
            transaction_id = transactionDetails['transaction_id']
            amount = transactionDetails['amount']
            mode_of_payment=transactionDetails['mode_of_payment']
            cur = mysql.connection.cursor()
            cur.execute("update transaction set amount=%s, mode_of_payment=%s where transaction_id=%s", (amount, mode_of_payment, transaction_id))
            mysql.connection.commit()
            cur.close()
        if request.form['trans'] == 'Delete':
            transactionDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            transaction_id = transactionDetails['transaction_id']
            # amount = transactionDetails['amount']
            # mode_of_payment=transactionDetails['mode_of_payment']
            cur = mysql.connection.cursor()
            cur.execute("delete from transaction where transaction_id = %s", (transaction_id))
            mysql.connection.commit()
            cur.close()

        return redirect('/transactionview')
    return render_template('transaction.html')

@app.route('/transactionview', methods=['GET', 'POST'])
def trans():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM transaction")
    if resultValue > 0:
        transactionDetails = cur.fetchall()
        return render_template('transactionview.html',transactionDetails=transactionDetails)

@app.route('/student_contact', methods=['GET', 'POST'])
def stuc():
    if request.method == 'POST':
        if request.form['stuc'] == 'Show Table':
            # Fetch form data
            return redirect('/student_cview')

        if request.form['stuc'] == 'Insert':
            # Fetch form data
            student_cDetails = request.form
            roll_no = student_cDetails['roll_no']
            contact = student_cDetails['contact']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO student_contact VALUES(%s, %s)",(roll_no, contact ))
            mysql.connection.commit()
            cur.close()
        if request.form['stuc'] == 'Update':
            student_cDetails = request.form
            roll_no = student_cDetails['roll_no']
            contact = student_cDetails['contact']
            cur = mysql.connection.cursor()
            cur.execute("update student_contact set contact=%s where roll_no=%s", (contact, roll_no))
            mysql.connection.commit()
            cur.close()
        if request.form['stuc'] == 'Delete':
            student_cDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            roll_no = student_cDetails['roll_no']
            contact = student_cDetails['contact']
            cur = mysql.connection.cursor()
            cur.execute("delete from student_contact where roll_no = %s and contact= %s", (roll_no, contact))
            mysql.connection.commit()
            cur.close()


        return redirect('/student_cview')
    return render_template('student_contact.html')

@app.route('/student_cview', methods=['GET', 'POST'])
def stucv():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM student_contact")
    if resultValue > 0:
        student_cDetails = cur.fetchall()
        return render_template('student_cview.html',student_cDetails=student_cDetails)


@app.route('/student_hostel_payment', methods=['GET', 'POST'])
def student_hostel_payment():
    if request.method == 'POST':
        if request.form['shp'] == 'Show Table':
            # Fetch form data
            return redirect('/stu_hostel_payview')

        if request.form['shp'] == 'Insert':
            # Fetch form data
            student_hostel_paymentDetails = request.form
            transaction_id = student_hostel_paymentDetails['transaction_id']
            roll_no = student_hostel_paymentDetails['roll_no']
            block_name =student_hostel_paymentDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO student_hostel_payment VALUES(%s, %s, %s)",(transaction_id, roll_no, block_name ))
            mysql.connection.commit()
            cur.close()
        if request.form['shp'] == 'Update':
            student_hostel_paymentDetails = request.form
            transaction_id = student_hostel_paymentDetails['transaction_id']
            roll_no = student_hostel_paymentDetails['roll_no']
            block_name =student_hostel_paymentDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("update student_hostel_payment set transaction_id=%s, block_name=%s where roll_no=%s", (transaction_id, block_name, roll_no))
            mysql.connection.commit()
            cur.close()
        if request.form['shp'] == 'Delete':
            student_hostel_paymentDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            transaction_id = student_hostel_paymentDetails['transaction_id']
            roll_no = student_hostel_paymentDetails['roll_no']
            block_name =student_hostel_paymentDetails['block_name']
            cur = mysql.connection.cursor()
            cur.execute("delete from student_hostel_payment where transaction_id = %s and roll_no= %s and block_name=%s", (transaction_id, roll_no, block_name))
            mysql.connection.commit()
            cur.close()



        return redirect('/stu_hostel_payview')
    return render_template('student_hostel_payment.html')

@app.route('/stu_hostel_payview', methods=['GET', 'POST'])
def shp():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM student_hostel_payment")
    if resultValue > 0:
        student_hostel_paymentDetails = cur.fetchall()
        return render_template('stu_hostel_payview.html', student_hostel_paymentDetails=student_hostel_paymentDetails)


@app.route('/staff', methods=['GET', 'POST'])
def staff():
    if request.method == 'POST':
        if request.form['stf'] == 'Show Table':
            # Fetch form data
            return redirect('/staffview')

        if request.form['stf'] == 'Insert':
            # Fetch form data
            staffDetails = request.form
            staff_id = staffDetails['staff_id']
            name = staffDetails['name']
            service=staffDetails['service']
            salary=staffDetails['salary']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO staff VALUES(%s, %s, %s, %s)",(staff_id, name, service, salary))
            mysql.connection.commit()
            cur.close()
        if request.form['stf'] == 'Update':
            staffDetails = request.form
            staff_id = staffDetails['staff_id']
            name = staffDetails['name']
            service=staffDetails['service']
            salary=staffDetails['salary']
            cur = mysql.connection.cursor()
            cur.execute("update staff set name=%s, service=%s, salary=%s where staff_id=%s", (name, service, salary, staff_id))
            mysql.connection.commit()
            cur.close()
        if request.form['stf'] == 'Delete':
            staffDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            staff_id = staffDetails['staff_id']
            # name = staffDetails['name']
            # service=staffDetails['service']
            # salary=staffDetails['salary']
            cur = mysql.connection.cursor()
            cur.execute("delete from staff where staff_id = %s", (staff_id))
            mysql.connection.commit()
            cur.close()

        return redirect('/staffview')
    return render_template('staff.html')

@app.route('/staffview', methods=['GET', 'POST'])
def stf():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM staff")
    if resultValue > 0:
        staffDetails = cur.fetchall()
        return render_template('staffview.html',staffDetails=staffDetails)


@app.route('/leave_rec', methods=['GET', 'POST'])
def leave_rec():
    if request.method == 'POST':
        if request.form['lea'] == 'Show Table':
            # Fetch form data
            return redirect('/leave_recview')

        if request.form['lea'] == 'Insert':
            # Fetch form data
            leave_recDetails = request.form
            record_no = leave_recDetails['record_no']
            in_time = leave_recDetails['in_time']
            out_time=leave_recDetails['out_time']
            roll_no=leave_recDetails['roll_no']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO leave_rec VALUES(%s, %s, %s, %s)",(record_no, in_time, out_time, roll_no))
            mysql.connection.commit()
            cur.close()
        if request.form['lea'] == 'Update':
            leave_recDetails = request.form
            record_no = leave_recDetails['record_no']
            in_time = leave_recDetails['in_time']
            out_time=leave_recDetails['out_time']
            roll_no=leave_recDetails['roll_no']
            cur = mysql.connection.cursor()
            cur.execute("update leave_rec set in_time=%s, out_time=%s, roll_no=%s where record_no=%s", (in_time, out_time, roll_no, record_no))
            mysql.connection.commit()
            cur.close()
        if request.form['lea'] == 'Delete':
            leave_recDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            record_no = leave_recDetails['record_no']
            # in_time = leave_recDetails['in_time']
            # out_time=leave_recDetails['out_time']
            # roll_no=leave_recDetails['roll_no']
            cur = mysql.connection.cursor()
            cur.execute("delete from leave_rec where record_no = %s", (record_no))
            mysql.connection.commit()
            cur.close()


        return redirect('/leave_recview')
    return render_template('leave_rec.html')

@app.route('/leave_recview', methods=['GET', 'POST'])
def lea():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM leave_rec")
    if resultValue > 0:
        leave_recDetails = cur.fetchall()
        return render_template('leave_recview.html',leave_recDetails=leave_recDetails)


@app.route('/staff_works_for', methods=['GET', 'POST'])
def staff_works_for():
    if request.method == 'POST':
        if request.form['swf'] == 'Show Table':
            # Fetch form data
            return redirect('/staff_works_forview')

        if request.form['swf'] == 'Insert':
            # Fetch form data
            staff_works_forDetails = request.form
            block_name = staff_works_forDetails['block_name']
            staff_id = staff_works_forDetails['staff_id']
            working_days=staff_works_forDetails['working_days']
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO staff_works_for VALUES(%s, %s, %s)",(block_name, staff_id, working_days))
            mysql.connection.commit()
            cur.close()
        if request.form['swf'] == 'Update':
            staff_works_forDetails = request.form
            block_name = staff_works_forDetails['block_name']
            staff_id = staff_works_forDetails['staff_id']
            working_days=staff_works_forDetails['working_days']
            cur = mysql.connection.cursor()
            cur.execute("update staff_works_for set working_days=%s, block_name=%s where staff_id=%s", (working_days, block_name, staff_id))
            mysql.connection.commit()
            cur.close()
        if request.form['swf'] == 'Delete':
            staff_works_forDetails = dict((key, request.form.getlist(key)) for key in request.form.keys())
            block_name = staff_works_forDetails['block_name']
            staff_id = staff_works_forDetails['staff_id']
            # working_days=staff_works_forDetails['working_days']
            cur = mysql.connection.cursor()
            cur.execute("delete from staff_works_for where block_name = %s and staff_id = %s", (block_name, staff_id))
            mysql.connection.commit()
            cur.close()
        return redirect('/staff_works_forview')
    return render_template('staff_works_for.html')

@app.route('/staff_works_forview', methods=['GET', 'POST'])
def swf():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM staff_works_for")
    if resultValue > 0:
        staff_works_forDetails = cur.fetchall()
        return render_template('staff_works_forview.html',staff_works_forDetails=staff_works_forDetails)

if __name__ == '__main__':
    app.run(debug=True)
