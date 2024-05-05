import price_info

def test_total_cost_shopping():
    quantity_list = {'apple': 10, 'orange': 5, 'watermelon': 1,
     'pineapple': 1, 'pear' : 4, 'papaya': 3, 'pomegranate': 2}
    result = price_info.total_cost_shopping()

    assert result == 50.55

def test_cost_of_fruit():
    print()