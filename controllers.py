import os
from flask import Flask, render_template, request, redirect
import requests
import xmltodict
import json
from datetime import date
from werkzeug.utils import secure_filename
from app import *
from models import *
from forms import *


@app.route('/search')
def search_function():
    
    searched = request.args.get('search', '')
    if searched:
        search_results = News.query.filter(News.title.contains(searched))
    return render_template('search.html', search_results = search_results, searched = searched)

@app.route("/")
def home():
    today = date.today().strftime("%d.%m.%Y")
    r = requests.get(f'https://www.cbar.az/currencies/{today}.xml')
    dict = xmltodict.parse(r.text)
    json_object = json.dumps(dict)
    y = json.loads(json_object)
    updated = y['ValCurs']['@Date']
    usd = y['ValCurs']['ValType'][1]['Valute'][0]['Value']
    eur = y['ValCurs']['ValType'][1]['Valute'][1]['Value']
    gbp = y['ValCurs']['ValType'][1]['Valute'][16]['Value']
    recent_news = News.query.order_by(News.date.desc()).limit(3)  
    return render_template('index.html', recent_news = recent_news, updated = updated, usd= usd, eur = eur, gbp = gbp)


@app.route("/online-queue", methods=['GET', 'POST'])
def online_queue():
    post_data = request.form
    form = QueueForm()
    if request.method == 'POST':
        form = QueueForm(data=post_data)
        if form.validate_on_submit():
            queue_requests = Queue(branch=form.branch.data, service=form.service.data, date=form.date.data, time=form.time.data, phone=form.phone.data)
            queue_requests.save()
            return redirect('/success')
    return render_template('online_queue.html', form = form)
    
@app.route('/success')
def successed():
    return render_template('success.html')


@app.route('/<filtr_category>')
def filtered_news_list(filtr_category):
    if filtr_category != 'xeberler-ve-elanlar' and filtr_category != 'bank' and filtr_category != 'investisiya' and filtr_category != 'korporativ':
        return redirect('/no-page')
    else:
        if filtr_category == 'xeberler-ve-elanlar':
            all_news = News.query.all()
        else:
            all_news = News.query.filter_by(category_name = filtr_category)      
        return render_template('news_list.html', all_news = all_news)


@app.route("/<int:news_id>")
def detailed_news(news_id):
    news = News.query.get(news_id)  
    similar_news = News.query.filter_by(category_name = news.category_name).limit(3)    
    return render_template('detailed_news.html', news = news, similar_news= similar_news)


@app.route('/ferdi-emanetler', methods=['POST', 'GET'])
def deposit_page():
    form = OnlineOrder()

    if request.method == 'POST':
        post_data = request.form
        form = OnlineOrder(data=post_data)

        if form.validate_on_submit():
            order = DepositOrder(first_name=form.first_name.data, last_name=form.last_name.data, deposit_type=form.deposit_type.data, mobile_number=form.mobile_number.data)
            order.save()

    deposits = Deposits.query.all()
    return render_template('deposit.html', deposits=deposits, form=form)



@app.route('/deposits/<deposit>')
def deposits_page(deposit):
    head = '/'+'deposits/'+deposit
    deposits = Deposits.query.filter_by(details_btn = head).all()
    deposits_names = Deposits_Names.query.filter_by(name = deposit).all()
    if len(deposits_names) == 1:
        dep_id = deposits_names[0].id
        deposits_info = DepositInfo.query.filter_by(deposit_id = dep_id).all()
        productTerms = ProductTerms.query.filter_by(deposit_id = dep_id).all()
        percentPaySpeed = PercentPaySpeed.query.filter_by(deposit_id = dep_id).all()
        monthly = PercentPaySpeed.query.filter_by(category = 'ayliq', deposit_id = dep_id).all()
        quarters = PercentPaySpeed.query.filter_by(category = 'rubluk', deposit_id = dep_id).all()
        endOfTerm = PercentPaySpeed.query.filter_by(category = 'muddetinsonu', deposit_id = dep_id).all()
        earlyEnds = EarlyEnd.query.filter_by(deposit_id = dep_id).all()
    else:
        return redirect('/no-page')
    return render_template('detailed_deposit.html', productTerms=productTerms, monthly=monthly, quarters=quarters, endOfTerm=endOfTerm, earlyEnds=earlyEnds, percentPaySpeed=percentPaySpeed, deposits=deposits, deposits_info=deposits_info)


@app.route('/category/<categoryName>')
def campaigns_page(categoryName):
    if categoryName == 'kampaniyalar-1':
        campaigns = Campaigns.query.all()
    else: 
        campaigns_category = Campaigns_category.query.filter_by(title = categoryName).all()
        if len(campaigns_category) == 1:
            campaigns = Campaigns.query.filter_by(category = categoryName).all()
        else:
            return redirect('/no-page')
    return render_template('campaigns.html', campaigns=campaigns, categoryName=categoryName)

@app.route('/no-page')
def no_page():
    return render_template('no_page.html')

@app.route('/card-order', methods=['POST', 'GET'])
def kartsifarisi_page():
    form = CardOrderForm()

    if request.method == 'POST':
        post_data = request.form
        form = CardOrderForm(data=post_data)

        if form.validate_on_submit():
            file1 = form.passport_front.data
            file2 = form.passport_back.data
            
            file1.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file1.filename)))
            file2.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(file2.filename)))

            sifaris = CardOrder(card_choose=form.card_choose.data, card_type=form.card_type.data, currency=form.currency.data, card_time=form.card_time.data, branch=form.branch.data, first_name=form.first_name.data, last_name=form.last_name.data, passport_front=form.passport_front.data, passport_back=form.passport_back.data, mobile_number=form.mobile_number.data, email=form.email.data)
            sifaris.save()
            return redirect('/success')
    return render_template('cardOrder.html', form=form)


