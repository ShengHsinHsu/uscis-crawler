from src import query_case_status
from src import psg_utils
import datetime
import time

count = 30000
docs = []
cols = ["case_no", "update_date", "status",
        "description", 'form', 'service_center']
none_count = 0

# update_date = datetime.datetime.utcnow()
update_date = '2021-10-10'

for case_no in query_case_status.generated_case_number('MSC', '219'):
    print('Case Number: {}'.format(case_no))
    data = query_case_status.query_case_status(case_no)
    
    for i, j in data.items():
        if i != 'case_no':
            print("{}: {}".format(i, j))
        
    data['update_date'] = update_date
    if data.get('status') and data.get('description'):
        print("Update to Postgres")
        psg_utils.update_case_status(cols=cols, data=data)
    else:
        none_count += 1
        
    if none_count == 100:
        exit()
        
    time.sleep(.5)
    print('\n-------------------------------------------------------\n')