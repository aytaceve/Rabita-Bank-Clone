from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, TelField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed


class QueueForm(FlaskForm):
    branch = SelectField(label = 'Filial', choices=[('Baş Ofis (Piramida plazanın 1-ci mərtəbəsi)', 'Baş Ofis (Piramida plazanın 1-ci mərtəbəsi)'), ('Nəsimi filialı (Heydər Əliyev sarayının yanı)', 'Nəsimi filialı (Heydər Əliyev sarayının yanı)'), ('Buta filialı (Amerika səfirliyinin yanı)', 'Buta filialı (Amerika səfirliyinin yanı)'), ('Kaspian filialı (Kaspian plazanın 1-ci mərtəbəsi)', 'Kaspian filialı (Kaspian plazanın 1-ci mərtəbəsi)'), ('Masallı filialı', 'Masallı filialı'), ('Naxçıvan şöbəsi', 'Naxçıvan şöbəsi'), ('Ağsu filialı', 'Ağsu filialı'), ('Nərimanov filialı (Funda klinikasının yanı)', 'Nərimanov filialı (Funda klinikasının yanı)'), ('Xətai filialı (Dəmirçi plazanın 1-ci mərtəbəsi)', 'Xətai filialı (Dəmirçi plazanın 1-ci mərtəbəsi)'), ('Ağcabədi filialı', 'Ağcabədi filialı'), ('Şirvan filialı', 'Şirvan filialı'), ('Şəmkir filialı', 'Şəmkir filialı'), ('Mərkəz filialı (İran səfirliyinin yanı)', 'Mərkəz filialı (İran səfirliyinin yanı)'), ('Xaçmaz filialı', 'Xaçmaz filialı'), ('Qusar filialı', 'Qusar filialı'), ('Səbail filialı (3-cü mkr dairəsinin yanı)', 'Səbail filialı (3-cü mkr dairəsinin yanı)'), ('Şamaxı filialı', 'Şamaxı filialı'), ('Gəncə filialı', 'Gəncə filialı'), ('Sahil filialı (Nərimanov m-nun yanı)', 'Sahil filialı (Nərimanov m-nun yanı)'), ('Şəki filialı', 'Şəki filialı'), ('Quba filialı', 'Quba filialı'), ('Kürdəmir filialı', 'Kürdəmir filialı'), ('Nizami filialı (Bakı kinoteatrının yanı)', 'Nizami filialı (Bakı kinoteatrının yanı)'), ('Lənkəran filialı', 'Lənkəran filialı'), ('Sumqayıt filialı', 'Sumqayıt filialı'), ('Yasamal filialı (Davinçi klinikasının yanı)', 'Yasamal filialı (Davinçi klinikasının yanı)')], validators=[DataRequired()], render_kw={'placeholder': 'Filial'})

    service = SelectField(label ='Xidmət növü', choices= [('Sürətli pul köçürmələri', 'Sürətli pul köçürmələri'), ('Western Union', 'Western Union'), ('Barat', 'Barat'), ('Zolotoya Korona', 'Zolotoya Korona'), ('Digər əməliyyatlar', 'Digər əməliyyatlar'), ('Onlayn kreditlər', 'Onlayn kreditlər'), ('İstehlak kreditləri', 'İstehlak kreditləri'), ('Lombard Krediti', 'Lombard Krediti'), ('Plastik kart', 'Plastik kart'), ('Onlayn kartın təhvil alınması', 'Onlayn kartın təhvil alınması'), ('Kart sifarişi', 'Kart sifarişi'), ('Kartın təhvil alınması', 'Kartın təhvil alınması'), ('Kredit ödənişi', 'Kredit ödənişi'), ('Əmanət', 'Əmanət'), ('Yeni əmanət', 'Yeni əmanət'), ('Digər əməliyyatlar', 'Digər əməliyyatlar'), ('Valyuta mübadiləsi', 'Valyuta mübadiləsi'), ('Satış', 'Satış'), ('Alışı', 'Alışı'), ('Hüquqi şəxs və sahibkarlar', 'Hüquqi şəxs və sahibkarlar'), ( 'Hüquqi şəxslər', 'Hüquqi şəxslər'), ('Fərdi sahibkarlar', 'Fərdi sahibkarlar'), ('Hesab üzrə əməliyyatlar', 'Hesab üzrə əməliyyatlar'), ('Mədaxil', 'Mədaxil'), ('Məxaric', 'Məxaric'), ('Hesab üzrə çıxarışın alınması', 'Hesab üzrə çıxarışın alınması'), ('Digər əməliyyatlar', 'Digər əməliyyatlar'),
    ('Kommunal və digər ödənişlər', 'Kommunal və digər ödənişlər'), ('Smart kart', 'Smart kart'), ('Digər əməliyyatlar', 'Digər əməliyyatlar'), ('Kassa əməliyyatları', 'Kassa əməliyyatları')], validators=[DataRequired()], render_kw={'placeholder': 'Xidmət növü'})

    date = DateField(label ='Tarix', validators=[DataRequired()], render_kw={'placeholder': 'Tarix'})

    time = SelectField('Vaxt', choices=[('10:00:00', '10:00:00'), ('11:00:00', '11:00:00'), ('12:00:00', '12:00:00'), ('13:00:00', '13:00:00'), ('14:00:00', '14:00:00'), ('15:00:00', '15:00:00'), ('16:00:00', '16:00:00')], validators= [DataRequired(message='Uyğun vaxtı seçin.')], render_kw={'placeholder': 'Vaxt'})
    phone = TelField(label = 'Mobil nömrə', validators=[DataRequired(message='Telefon nömrənizi daxil edin.')], render_kw={'placeholder': 'Mobil nömrə'})

class SearchForm(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
   

class OnlineOrder(FlaskForm):
    first_name = StringField(label='Adınız', validators=[DataRequired(), Length(max=30)])
    last_name = StringField(label='Soyadınız', validators=[DataRequired(), Length(max=30)] )
    deposit_type = SelectField(label='Əmanət növü seçin', validators=[DataRequired()], choices = [('Universal Əmanət', 'Universal Əmanət'), ('Uşaq yığım əmanəti', 'Uşaq yığım əmanəti'), ('Saxlanc seyfləri', 'Saxlanc seyfləri')])
    mobile_number = StringField(label='Mobil nömrə', validators=[DataRequired()])


class CardOrderForm(FlaskForm):
    card_choose = SelectField(label='Kart seçin', validators=[DataRequired()], choices = [('Kartmane Debet', 'Kartmane Debet')])
    card_type = SelectField(label='Kart növü', validators=[DataRequired()], choices = [('Mastercard', 'Mastercard'), ('Visa', 'Visa')])
    currency = SelectField(label='Valyuta', validators=[DataRequired()], choices = [('AZN', 'AZN'),('USD', 'USD'),('EUR', 'EUR')])
    card_time = SelectField(label='Kartın müddəti', validators=[DataRequired()], choices = [('5 il', '5 il')])
    branch = SelectField(label='Filial', validators=[DataRequired()], choices = [('Baş Ofis (Piramida plazanın 1-ci mərtəbəsi)', 'Baş Ofis (Piramida plazanın 1-ci mərtəbəsi)'),('Nəsimi filialı (Heydər Əliyev sarayının yanı)', 'Nəsimi filialı (Heydər Əliyev sarayının yanı)'),('Buta filialı (Amerika səfirliyinin yanı)', 'Buta filialı (Amerika səfirliyinin yanı)'),('Kaspian filialı (Kaspian plazanın 1-ci mərtəbəsi)', 'Kaspian filialı (Kaspian plazanın 1-ci mərtəbəsi)'),('Masallı filialı', 'Masallı filialı'),('Qaradağ filialı', 'Qaradağ filialı'),('Ağsu filialı', 'Ağsu filialı'),('Nərimanov filialı (Funda klinikasının yanı)', 'Nərimanov filialı (Funda klinikasının yanı)'),('Xətai filialı (Dəmirçi plazanın 1-ci mərtəbəsi)', 'Xətai filialı (Dəmirçi plazanın 1-ci mərtəbəsi)'),('Ağcabədi filialı', 'Ağcabədi filialı'),('Şirvan filialı', 'Şirvan filialı'),('Şəmkir filialı', 'Şəmkir filialı'),('Mərkəz filialı (İran səfirliyinin yanı)', 'Mərkəz filialı (İran səfirliyinin yanı)'),('Xaçmaz filialı', 'Xaçmaz filialı'),('Qusar filialı', 'Qusar filialı'),('Səbail filialı (3-cü mkr dairəsinin yanı)', 'Səbail filialı (3-cü mkr dairəsinin yanı)'),('Şamaxı filialı', 'Şamaxı filialı'),('Gəncə filialı', 'Gəncə filialı'),('Sahil filialı (Nərimanov m-nun yanı)', 'Sahil filialı (Nərimanov m-nun yanı)'),('Şəki filialı', 'Şəki filialı'),('Quba filialı', 'Quba filialı'),('Kürdəmir filialı', 'Kürdəmir filialı'),('Nizami filialı (Bakı kinoteatrının yanı)', 'Nizami filialı (Bakı kinoteatrının yanı)'),('Lənkəran filialı', 'Lənkəran filialı'),('Sumqayıt filialı', 'Sumqayıt filialı'),('Yasamal filialı (Davinçi klinikasının yanı)', 'Yasamal filialı (Davinçi klinikasının yanı)'),('Naxçıvan şöbəsi', 'Naxçıvan şöbəsi')])
    first_name = StringField(label='Adınız', validators=[DataRequired(), Length(max=30)])
    last_name = StringField(label='Soyadınız', validators=[DataRequired(), Length(max=30)])
    passport_front = FileField(label='Şəxsiyyət vəsiqənizin ön üzü', validators=[FileRequired(), FileAllowed(['png', 'jpg'], "Zəhmət olmasa şəkil formatı yükləyin!")])
    passport_back = FileField(label='Şəxsiyyət vəsiqənizin arxa üzü', validators=[FileRequired(), FileAllowed(['png', 'jpg'], "Zəhmət olmasa şəkil formatı yükləyin!")])
    mobile_number = StringField(label='Mobil nömrə', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=3, max=30)])

class RegisterForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(min=3, max=30)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=3, max=30)])
    username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=8, max=30)])

class LoginForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField(label='Password', validators=[DataRequired(), Length(min=8, max=30)])
