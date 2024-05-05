import price_info

def test_total_cost_shopping():
    quantity_list = {'apple': 10, 'orange': 5, 'watermelon': 1,
     'pineapple': 1, 'pear' : 4, 'papaya': 3, 'pomegranate': 2}
    result = price_info.total_cost_shopping(quantity_list)

    assert result == 50.550000000000004

def test_cost_of_fruit():
    result = price_info.cost_of_fruits('papaya', 5)

    assert result == 14.75