# Stores by location (default distance is 10km)
r'/stores/(?P<lat>[0-9]{2}\.[0-9]{3})/(?P<long>[0-9]{2}\.[0-9]{3})/(?P<query>[\w-\\\.\']{2,50})/{token}/'
r'/stores/(?P<lat>[0-9]{2}\.[0-9]{3})/(?P<long>[0-9]{2}\.[0-9]{3})/(?P<query>[\w-\\\.\']{2,50})/{token}/?P<distance>[0-9]{1,5}'

# Store products
/stores/{id}/products/{token}/

# Products list
/products/{token}/
