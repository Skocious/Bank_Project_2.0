from data_access_layer.customer_dao_access.customer_dao_imp import CustomerDAOImp
from service_layer.customer_service_layer.customer_service_imp import CustomerServiceImp


customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

