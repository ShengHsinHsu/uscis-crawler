from bs4 import BeautifulSoup
import requests
import re

url = 'https://egov.uscis.gov/casestatus/mycasestatus.do'


def query_case_status(case_no):
    service_center = case_no[:3]
    form_data = {
        "changeLocale": None,
        'completedActionsCurrentPage': '0',
        'upcomingActionsCurrentPage': '0',
        'appReceiptNum': str(case_no),
        'caseStatusSearchBtn': 'CHECK STATUS'
    }
    res = requests.post(url, data=form_data)
    soup = BeautifulSoup(res.content, "html.parser")

    msg = soup.findAll('div', {'class': 'rows text-center'})[0]
    description = msg.p.text
    status = msg.h1.text
    form = re.search('(I-(\d+))', description)
    form = 'Unknown' if not form else form.group(1)
    return {
        'case_no': case_no,
        'status': status,
        'description': description,
        'form': form,
        'service_center': service_center
    }


def generated_case_number(service_center, fy, number=1):
    max_number_len = 7
    while True:
        n_str = str(number)
        len_n_str = len(n_str)
        if len_n_str > 7:
            break
        
        for _ in range(max_number_len - len_n_str):
            n_str = '0' + n_str
            
        number += 1
        yield '{service_center}{fy}{n_str}'.format(
            service_center=service_center,
            fy=fy,
            n_str=n_str,

        )
