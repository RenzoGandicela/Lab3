import employee_info

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(13, 30)

    assert result == [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]

def test_calculate_average_salary():
    test_data = [
        {"name": "Vignesh", "age": 12, "department": "Sales", "salary": 20000},
        {"name": "Zikang", "age": 30, "department": "Engineering", "salary": 60000},
        {"name": "John", "age": 30, "department": "Engineering", "salary": 40000}
    ]
    result = employee_info.calculate_average_salary(test_data)

    assert result == 40000

def test_get_employees_by_dept():
    test_data = [
        {"name": "Vignesh", "age": 12, "department": "Sales", "salary": 20000},
        {"name": "Zikang", "age": 30, "department": "Engineering", "salary": 60000},
        {"name": "John", "age": 30, "department": "Engineering", "salary": 40000}
    ]
    result = employee_info.get_employees_by_dept(test_data, "Engineering")

    assert result == [
        {"name": "Zikang", "age": 30, "department": "Engineering", "salary": 60000},
        {"name": "John", "age": 30, "department": "Engineering", "salary": 40000}
    ]