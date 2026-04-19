@app.route('/result9', methods=['GET', 'POST'])
def result9():
    res = None
    
    if request.method == 'POST':
        phone = request.form.get('phone', '').strip()
        date = request.form.get('date', '').strip()

        if (phone.startswith('+') and len(phone) >= 11 and date):
            res = [phone, date]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result9.html', res=res)
