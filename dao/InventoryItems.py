'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from model.InventoryItems import InventoryItems
from util.db_helper import db_transaction


@db_transaction
def get_item_details(session):
    resultL = []
    itemDetails = session.query(InventoryItems.item_id,InventoryItems.item_number,InventoryItems.item_type,InventoryItems.description,InventoryItems.long_description,
                                        InventoryItems.transaction_uom,InventoryItems.conversion,InventoryItems.base_uom).filter(InventoryItems.enabled_flag=='Y').all()
                  
    for itemDetail in itemDetails:
        dict ={ }
        dict['item_id'] = itemDetail[0]
        dict['item_number'] = itemDetail[1]
        dict['item_type'] = itemDetail[2]
        dict['description'] = itemDetail[3]
        dict['long_description'] = itemDetail[4]
        dict['transaction_uom'] = itemDetail[5]
        dict['conversion'] = itemDetail[6]
        dict['base_uom'] = itemDetail[7]
        
        resultL.append(dict)    
            
    return resultL