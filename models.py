from extensions import *
from controllers import *


class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text(), nullable=False)
    news_content = db.Column(db.Text(), nullable=False)
    image_status = db.Column(db.Boolean(), nullable=True)
    image_url = db.Column(db.String(255))
    date = db.Column(db.Date(), nullable=False)
    category_name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.title

    def __init__(self, title, news_content, image_status, image_url, date, category_name):
        self.title = title
        self.news_content = news_content
        self.image_status = image_status
        self.image_url = image_url
        self.date = date
        self.category_name = category_name

    def save(self):
        db.session.add(self)
        db.session.commit()

class Queue(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    branch = db.Column(db.Text(), nullable=False)
    service = db.Column(db.Text(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    time = db.Column(db.Time(), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    
    def __repr__(self):
        return self.branch

    def __init__(self, branch, service, date, time, phone):
        self.branch = branch
        self.service = service
        self.date = date
        self.time = time
        self.phone = phone

    def save(self):
        db.session.add(self)
        db.session.commit()
  

class Deposits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)
    details_btn = db.Column(db.String(100), nullable=False)
    term = db.Column(db.String(10))
    percent = db.Column(db.String(10))

    def __repr__(self):
        return self.title
    
    def __init__(self, title, image_url, details_btn, term, percent):
        self.title = title
        self.image_url = image_url
        self.details_btn = details_btn
        self.term = term
        self.percent = percent

    def save(self):
        db.session.add(self)
        db.session.commit()


class DepositOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    deposit_type = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.first_name

    def __init__(self, first_name, last_name, deposit_type, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.deposit_type = deposit_type
        self.mobile_number = mobile_number
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.title

    def __init__(self, title, image_url, details, category):
        self.title = title
        self.image_url = image_url
        self.details = details
        self.category = category
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Campaigns_category(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return self.title

    def __init__(self, title):
        self.title = title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class CardOrder(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    card_choose = db.Column(db.String(100), nullable=False)
    card_type = db.Column(db.String(100), nullable=False)
    currency = db.Column(db.String(100), nullable=False)
    card_time = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    passport_front = db.Column(db.String(100), nullable=False)
    passport_back = db.Column(db.String(100), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return self.first_name

    def __init__(self, card_choose, card_type, currency, card_time, branch, first_name, last_name, passport_front, passport_back, mobile_number, email):
        self.card_choose = card_choose
        self.card_type = card_type
        self.currency = currency
        self.card_time = card_time
        self.branch = branch
        self.first_name = first_name
        self.last_name = last_name
        self.passport_front = passport_front
        self.passport_back = passport_back
        self.mobile_number = mobile_number
        self.email = email
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Deposits_Names(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    product_terms = db.relationship('ProductTerms', backref='Deposits_Names')
    percent_pay_speed = db.relationship('PercentPaySpeed', backref='Deposits_Names')
    early_end = db.relationship('EarlyEnd', backref='Deposits_Names')
    deposit_info = db.relationship('DepositInfo', backref='Deposits_Names')

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    
    def save(self):
        db.session.add(self)
        db.session.commit()

class DepositInfo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    info = db.Column(db.String(300))
    deposit_id = db.Column(db.Integer(), db.ForeignKey(Deposits_Names.id))

    def __repr__(self):
        return self.info

    def __init__(self,info, deposit_id):
        self.info = info
        self.deposit_id = deposit_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class ProductTerms(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    value = db.Column(db.String(300), nullable=False)
    deposit_id = db.Column(db.Integer(), db.ForeignKey(Deposits_Names.id))

    def __repr__(self):
        return self.title

    def __init__(self, title, value, deposit_id):
        self.title = title
        self.value = value
        self.deposit_id = deposit_id 
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
class PercentPaySpeed(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    term = db.Column(db.String(30), nullable=False)
    azn = db.Column(db.String(10), nullable=False)
    usd = db.Column(db.String(10), nullable=False)
    eur = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    deposit_id = db.Column(db.Integer(), db.ForeignKey(Deposits_Names.id))


    def __repr__(self):
        return self.muddet

    def __init__(self, term, azn, usd, eur, category, deposit_id):
        self.term = term
        self.azn = azn
        self.usd = usd
        self.eur = eur
        self.category = category
        self.deposit_id = deposit_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class EarlyEnd(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    term = db.Column(db.String(30), nullable=False)
    azn = db.Column(db.String(10), nullable=False)
    usd = db.Column(db.String(10), nullable=False)
    eur = db.Column(db.String(10), nullable=False)
    deposit_id = db.Column(db.Integer(), db.ForeignKey(Deposits_Names.id))

    def __repr__(self):
        return self.term

    def __init__(self, term, azn, usd, eur, deposit_id):
        self.term = term
        self.azn = azn
        self.usd = usd
        self.eur = eur
        self.deposit_id = deposit_id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

admin.add_view(ModelView(News, db.session))
admin.add_view(ModelView(Queue, db.session))
admin.add_view(ModelView(Deposits, db.session))
admin.add_view(ModelView(DepositOrder, db.session))
admin.add_view(ModelView(Campaigns, db.session))
admin.add_view(ModelView(CardOrder, db.session))

