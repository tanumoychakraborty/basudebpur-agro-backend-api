'''
Created on 22-Dec-2018

@author: duttasudip89
'''
from model.InventoryItems import InventoryItems
from util.db_helper import db_transaction
from sqlalchemy.sql.expression import and_
from falcon.http_error import HTTPError
from falcon import status_codes

''' item search with different parameter '''
@db_transaction
def search_item_details(params,page, page_size,session):
    resultL = []
    item_number = params.get('item_number',None)
    item_type = params.get('item_type',None)
    description = params.get('description',None)
    enabled_flag = params.get('enabled_flag',None)
    
    
    itemDetails = session.query(InventoryItems.item_id,InventoryItems.item_number,InventoryItems.item_type,InventoryItems.description,InventoryItems.long_description,
                                           InventoryItems.transaction_uom,InventoryItems.conversion,InventoryItems.base_uom,InventoryItems.enabled_flag)
    
    conditions = []
    if item_number:
            conditions.append(InventoryItems.item_number == item_number)
    if item_type:
            conditions.append(InventoryItems.item_type == item_type)
    if description:
            conditions.append(InventoryItems.description == description)
    if enabled_flag:
            conditions.append(InventoryItems.enabled_flag == enabled_flag)        
            
                
    itemDetails = itemDetails.filter(and_(*conditions)).all()   
        
    if page_size:
            itemDetails = itemDetails.limit(page_size)
    if page: 
            itemDetails = itemDetails.offset(page*page_size) 
                  
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
        dict['enabled_flag'] = itemDetail[8]
    
        resultL.append(dict)    
            
    return resultL

''' fetch single item details by passing item number '''
@db_transaction
def get_item_detail(item_number,session):
    item = session.query(InventoryItems).filter_by(item_number=item_number).first()
    result = dict(item.__dict__)
    result.pop('_sa_instance_state')
    return result 

'''drill down to specific item details from search screen'''
@db_transaction
def get_item_details(session):
    resultL = []
    itemDetails = session.query(InventoryItems).all()
                  
    for itemDetail in itemDetails:
        dict ={ }
        dict['item_id'] = itemDetail.item_id
        dict['item_number'] = itemDetail.item_number
        dict['item_type'] = itemDetail.item_type
        dict['description'] = itemDetail.description
        dict['long_description'] = itemDetail.long_description
        dict['transaction_uom'] = itemDetail.transaction_uom
        dict['conversion'] = itemDetail.conversion
        dict['base_uom'] = itemDetail.base_uom
        dict['enabled_flag'] = itemDetail.enabled_flag
        resultL.append(dict)     

            
    return resultL 

@db_transaction
def create_items(raw_data, session):
    inventoryItems = InventoryItems()
    if 'item_number' in raw_data:
        inventoryItems.item_number = raw_data['item_number']
    if 'item_type' in raw_data:
        inventoryItems.item_type = raw_data['item_type']
    if 'description' in raw_data:
        inventoryItems.description = raw_data['description']
    if 'long_description' in raw_data:
        inventoryItems.long_description = raw_data['long_description']
    if 'transaction_uom' in raw_data:
        inventoryItems.remarks = raw_data['transaction_uom']
    if 'conversion' in raw_data:
        inventoryItems.conversion = raw_data['conversion']
    if 'base_uom' in raw_data:
        inventoryItems.base_uom = raw_data['base_uom'] 
    if 'enabled_flag' in raw_data:
        inventoryItems.enabled_flag = raw_data['enabled_flag']
    inventoryItems.created_by = raw_data['created_by']
    inventoryItems.last_updated_by = raw_data['last_updated_by'] 
    
    session.add(inventoryItems)
    
    return inventoryItems

@db_transaction
def update_items(raw_data,session):
    item_number = raw_data['item_number']
    inventoryItems = session.query(InventoryItems).filter_by(item_number=item_number).first()
    if inventoryItems is None:
        raise HTTPError(status=status_codes.HTTP_404, errors="Item Details does not exist")
    
    if 'item_number' in raw_data:
        inventoryItems.item_number = raw_data['item_number']
    if 'item_type' in raw_data:
        inventoryItems.item_type = raw_data['item_type']
    if 'description' in raw_data:
        inventoryItems.description = raw_data['description']
    if 'long_description' in raw_data:
        inventoryItems.long_description = raw_data['long_description']
    if 'transaction_uom' in raw_data:
        inventoryItems.remarks = raw_data['transaction_uom']
    if 'conversion' in raw_data:
        inventoryItems.conversion = raw_data['conversion']
    if 'base_uom' in raw_data:
        inventoryItems.base_uom = raw_data['base_uom'] 
    if 'enabled_flag' in raw_data:
        inventoryItems.enabled_flag = raw_data['enabled_flag']
    inventoryItems.last_updated_by = raw_data['last_updated_by'] 
    
    