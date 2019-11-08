import logging
from flask import render_template, Response, request, jsonify, redirect, url_for
from app import app
from app.methods import get_index, get_value, set_value, add_to_list, add_data, delete_data, search, get_items_by_id, get_items_by_category, read_data, write_data
from app.buyers import buyers, buyers_index, buyers_search_items
from app.items import items, items_index
from app.users import users, users_index
from app.sellers import sellers_search_items, sellers, initiate_sellers

users = read_data("users")

current_user = users[1]

write_data("current_user", current_user)

initiate_sellers(users)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')

@app.route('/sell', methods=['GET', 'POST'])
def sell():
	global items
	global current_user
	global sellers_search_items

	items = read_data("items")
	current_user = read_data("current_user")

	sellers_search_items = []

	seller_item_ids = get_value(current_user, 'items_list')

	seller_items = []

	get_items_by_id("items", items, seller_item_ids, seller_items)

	if request.method == 'POST':

		search("sellers_search_items", sellers_search_items, items)

		return jsonify(sellers_search_items = sellers_search_items)
	else:
		return render_template('sell.html', current_user = current_user, items = items, sellers_search_items = sellers_search_items) 

@app.route('/cart', methods=['GET', 'POST'])
def cart():
	global current_user
	global items

	items = read_data("items")
	current_user = read_data("current_user")

	cart_items = get_value(current_user, 'buyer')

	return render_template('cart.html', cart_items = cart_items, items = items, current_user = current_user)

@app.route('/buy', methods=['GET', 'POST'])
def buy():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	return render_template('buy.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)

@app.route('/buy/all', methods=['GET', 'POST'])
def all():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	if request.method == 'POST':

		buyers_search_items = []

		search("buyers_search_items", buyers_search_items, items)

		return jsonify(buyers_search_items = buyers_search_items)
	else:
		return render_template('all.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)

@app.route('/buy/household', methods=['GET', 'POST'])
def household():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	if request.method == 'POST':

		buyers_search_items = []

		search("buyers_search_items", buyers_search_items, household_items)

		return jsonify(buyers_search_items = buyers_search_items)
	else:
		return render_template('household.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)

@app.route('/buy/furniture', methods=['GET', 'POST'])
def furniture():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	if request.method == 'POST':

		buyers_search_items = []

		search("buyers_search_items", buyers_search_items, furniture_items)

		return jsonify(buyers_search_items = buyers_search_items)
	else:
		return render_template('furniture.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)


@app.route('/buy/electronics', methods=['GET', 'POST'])
def electronics():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	if request.method == 'POST':

		buyers_search_items = []

		search("buyers_search_items", buyers_search_items, electronics_items)

		return jsonify(buyers_search_items = buyers_search_items)
	else:
		return render_template('electronics.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)


@app.route('/buy/appliances', methods=['GET', 'POST'])
def appliances():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	if request.method == 'POST':

		buyers_search_items = []

		search("buyers_search_items", buyers_search_items, appliances_items)

		return jsonify(buyers_search_items = buyers_search_items)
	else:
		return render_template('appliances.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)


@app.route('/buy/tools', methods=['GET', 'POST'])
def tools():
	global items
	global current_user
	global users
	global buyers_search_items

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	household_items = []
	furniture_items = []
	electronics_items = []
	appliances_items = []
	tools_items = []

	get_items_by_category(items, 'household', household_items)
	get_items_by_category(items, 'furniture', furniture_items)
	get_items_by_category(items, 'electronics', electronics_items)
	get_items_by_category(items, 'appliances', appliances_items)
	get_items_by_category(items, 'tools', tools_items)

	if request.method == 'POST':

		buyers_search_items = []

		search("buyers_search_items", buyers_search_items, tools_items)

		return jsonify(buyers_search_items = buyers_search_items)
	else:
		return render_template('tools.html', items = items, current_user = current_user, users = users, buyers_search_items = buyers_search_items, household_items = household_items, furniture_items = furniture_items, electronics_items = electronics_items, appliances_items = appliances_items, tools_items = tools_items)


@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
	global items_index
	global current_user
	global items

	items = read_data("items")
	current_user = read_data("current_user")

	items_index = get_index(items)

	if request.method == 'POST':
		add_data(items_index)
		return jsonify(items = items)
	else:
		return render_template('add_item.html', items_index = items_index)

@app.route('/add_to_cart', methods=['GET', 'POST'])
def add_to_cart():
	global buyers
	global buyers_index
	global current_user

	json_data = request.get_json()
	item_id = json_data["item_id"]
	user_id = json_data["user_id"]
	seller = json_data["seller"]
	title = json_data["title"]

	buyer = get_value(current_user, 'user')
	current_user = read_data("current_user")

	new_buyer_entry = {
	    "item_id": item_id,
	    "user_id": user_id,
	    "seller": seller,
	    "title": title,
	    "buyer": buyer,
	}

	add_to_list("buyers", buyers, new_buyer_entry, len(buyers))

	buyers = read_data("buyers")

	set_value(current_user, 'buyer', item_id)

	current_user = read_data("current_user")

	return jsonify(buyers = buyers)

@app.route('/send_message', methods=['GET', 'POST'])
def send_message():

	global current_user

	current_user = read_data("current_user")

	json_data = request.get_json()
	message_text = json_data["message_text"]
	user_id = json_data["user_id"]
	seller = json_data["seller"]

	messages = get_value(current_user, 'messages')
	current_user = read_data("current_user")

	new_message = {
	    "message_text": message_text,
	    "user_id": user_id,
	    "seller": seller
	}

	set_value(current_user, 'messages', new_message)

	current_user = read_data("current_user")

	return jsonify(current_user = current_user)

@app.route('/view_item/<item_id>', methods=['GET', 'POST'])
def view_item(item_id):
	item_id = item_id
	if request.method == 'POST':
		return redirect(url_for('item', item_id = item_id))
	return render_template('item.html')

@app.route('/item/<item_id>', methods=['GET', 'POST'])
def item(item_id):
	global current_user
	global items
	global users

	items = read_data("items")
	users = read_data("users")
	current_user = read_data("current_user")

	item_id = item_id

	index = int(item_id)

	item = items[index]

	return render_template('item.html', item = item, current_user = current_user, items = items, users = users)
  
@app.route('/update_item/<item_id>', methods=['GET', 'POST'])
def update_item(item_id):

	item_id = item_id
	
	current_item = {}

	for item in items:
		for key, value in item.items():
			if (key == 'item_id'):
				if(item_id == str(value)):
					current_item = item

	if request.method == 'POST':
		add_data(item_id)

		return jsonify(items = items)
	else:
		return render_template('update_item.html', current_item  = current_item)

@app.route('/remove_from_cart/<item_id>', methods=['GET', 'POST'])
def remove_from_cart(item_id):
	global current_user
	global buyers

	current_user = read_data("current_user")

	if request.method == 'POST':

		delete_data(current_user, 'buyer', "buyers", buyers, item_id)

		return redirect(url_for('cart'))
	return render_template('cart.html')

@app.route('/delete/<item_id>', methods=['GET', 'POST'])
def delete(item_id):
	global current_user
	global items

	items = read_data("items")
	current_user = read_data("current_user")

	delete_data(current_user, 'items_list', "items", items, item_id)

	return redirect(url_for('sell'))
