import Lab2.bmi as BMI

def test_bmi_normal_weight():
    assert (BMI.calculate_bmi(1.60,50) == 0)

def test_bmi_under_weight():
    assert (BMI.calculate_bmi(1.60,30) == -1)

def test_bmi_over_weight():
    assert (BMI.calculate_bmi(1.73,80) == 1)