# -file- PARAMETERS.py

# POST parameters for delivery address
address_params = {'ordertimenowlater':'now',
'Customer.UnitNo':'',
'Customer.StreetNo':'',
'Customer.Street':'',
'Customer.Suburb':'',
'Customer.Postcode':''}

address_request_headers = {'Host': 'order.dominos.com.au',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://order.dominos.com.au/estore/en/CustomerDetails/Delivery',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': 141,
'Origin': 'https://order.dominos.com.au',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': 1}

delivery_url = 'https://order.dominos.com.au/estore/en/Home?redirectTo=delivery'
delivery_posturl = 'https://order.dominos.com.au/estore/en/DeliverySearch/AllDetails'
delivery_confirm_url = ''
site_order_base = 'https://order.dominos.com.au/'
site_base = 'https://www.dominos.com.au/'

init_request_headers = {'Host': 'www.dominos.com.au',
#'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
#'Referer': 'https://duckduckgo.com/',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'}

ASP_NET_sessionid = ''
init_cookie = ''

# ALL OF THE NECESSARY COOKIES TO GET TO PRODUCT MENU
{"_sp_id.df43":"",
"_sp_ses.df43":"",
"ai_session":"",
"ai_user":"",
"akaalb_dominos-australia-alb":"",
"ARRAffinity":"",
"ASP.NET_SessionId":"",
"clearBasket":"",
"FormattedAddress":"",
"Language":"en",
"MenuHash":"",
"Menus":"",
"OrderTime":"asap",
"ServiceMethod":"",
"StoreName":"",
"StoreNumber":""}
