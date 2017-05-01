'''
Created on May 1, 2017

@author: Akhil Mathew
'''

stage_choice = (('new','New'),('progress','In progress'),('matured','Matured'),('dead','Dead'))

priority_choice = (('low','Low'),('normal','Normal'),('high','High'),('veryhigh','Very High'))

sale_order_state = (('draft', 'Draft Quotation'),('sent', 'Quotation Sent'),('cancel', 'Cancelled'),
            ('waiting_date', 'Waiting Schedule'),('progress', 'Sales Order'),('manual', 'Sale to Invoice'),
            ('shipping_except', 'Shipping Exception')('invoice_except', 'Invoice Exception'),('done', 'Done'))

shipping_policy = (('direct','Deliver each product when available'),('one','Deliver all products at once'))

unit_choice = (('unit','Unit'),('weight','Weight'),('volume','Volume'),('length','Length'),('time','Time'))

product_type_choices = (('stockable','Stockable'),('consumable','Consumable'),('service','Service'))

status = (('development','In developemt'),('normal','Normal'),('end','End of Life Cycle'),('obsolete','Obsolote'))
    
