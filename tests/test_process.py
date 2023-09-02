from src.functions.process import extractWeatherData, splitWeatherData, extractWeatherTime, splitWeatherTime
from tests.fixture import test_data_extract, test_data_split, test_weather_split

def test_extractWeatherData(test_data_extract):
    real = extractWeatherData(test_data_extract)
    expect = ([{'elementName': 'Wx', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '多雲', 'parameterValue': '4'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '晴時多雲', 'parameterValue': '2'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '晴時多雲', 'parameterValue': '2'}}]}], [{'elementName': 'PoP', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '20', 'parameterUnit': '百分比'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '10', 'parameterUnit': '百分比'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '10', 'parameterUnit': '百分比'}}]}], [{'elementName': 'MinT', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '29', 'parameterUnit': 'C'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '25', 'parameterUnit': 'C'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '25', 'parameterUnit': 'C'}}]}], [{'elementName': 'MaxT', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '32', 'parameterUnit': 'C'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '29', 'parameterUnit': 'C'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '32', 'parameterUnit': 'C'}}]}])

    assert real == expect

def test_splitWeatherData(test_data_split):
    real = splitWeatherData(test_data_split)
    expect = (['多雲', '晴時多雲', '晴時多雲'], ['20', '10', '10'], ['29', '25', '25'], ['32', '29', '32'])

    assert real == expect


def test_extractWeatherTime(test_data_extract):
    real = extractWeatherTime(test_data_extract)
    expect = (['2023-08-26 12:00:00', '2023-08-26 18:00:00', '2023-08-27 06:00:00'], ['2023-08-26 18:00:00', '2023-08-27 06:00:00', '2023-08-27 18:00:00']) 

    assert real == expect

def test_splitWeatherTime(test_weather_split):
    real = splitWeatherTime(test_weather_split)
    expect = ['08/26 12:00 - 08/26 18:00', '08/26 18:00 - 08/27 06:00', '08/27 06:00 - 08/27 18:00']

    assert real == expect


