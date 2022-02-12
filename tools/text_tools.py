import re


def remove_dates(text, replace_with=''):
    return re.sub('\d{1,2}\.\d{1,2}\.\d{4}', replace_with, text)


def remove_latin(text, replace_with=''):
    return re.sub('[a-zA-Z]', replace_with, text)

def mask_age(text, mask='<AGE>'):
    # return re.sub(r"(\d+) \byear\b", mask, text)
    for group in re.findall(r"(\d+) year", text):
        text = text.replace(group, mask)
    return text

def keep_only_ru(text, replace_with=''):
    return re.sub('[^а-яА-Я\s.]', replace_with, text)


def sanitize(text):
    text = text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
    text = re.sub(' +', ' ', text)
    return text.strip()


def sanitize_ru_text(text):
    text = text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
    text = re.sub(' +', ' ', text)
    text = re.sub('[^а-яА-Я\s.,\d]', '', text)
    return text.strip()

def process_ru(text):
    sanitaized = sanitize_ru_text(text).replace(
        ' г ', ' ').replace(' я ', '').replace('яя', '')

    sanitaized = remove_dates(sanitaized, replace_with='<DATE>')
    sanitaized = '. '.join([i.strip()
                            for i in sanitaized.split('.') if i.strip()])
    sanitaized = ', '.join([i.strip()
                            for i in sanitaized.split(',') if i.strip()])
    sanitaized = ' '.join([i.strip()
                           for i in sanitaized.split(' ') if i.strip()])
    return sanitaized

def process_en(text):
    sanitaized = sanitize(text.capitalize()).replace(' y.o. ', ' year old ').replace(
        'yo ', ' year old ').replace(' y.o ', ' year old ').replace('-year-old', ' year old ')
        
    sanitaized = remove_dates(sanitaized, replace_with='<DATE>')
    sanitaized = '. '.join([i.strip()
                            for i in sanitaized.split('.') if i.strip()])
    sanitaized = ', '.join([i.strip()
                            for i in sanitaized.split(',') if i.strip()])
    sanitaized = ' '.join([i.strip()
                           for i in sanitaized.split(' ') if i.strip()])
    sanitaized = ' ('.join([i.strip()
                            for i in sanitaized.split('(') if i.strip()])
    sanitaized = ') '.join([i.strip()
                            for i in sanitaized.split(')') if i.strip()])
                            
    sanitaized = mask_age(sanitaized)
    return sanitaized
