import pytest

@pytest.fixture()
def test_data_extract():
    return {
            "success": "true",
            "result": {
                "resource_id": "F-C0032-001",
                "fields": [
                {
                    "id": "datasetDescription",
                    "type": "String"
                },
                {
                    "id": "locationName",
                    "type": "String"
                },
                {
                    "id": "parameterName",
                    "type": "String"
                },
                {
                    "id": "parameterValue",
                    "type": "String"
                },
                {
                    "id": "parameterUnit",
                    "type": "String"
                },
                {
                    "id": "startTime",
                    "type": "Timestamp"
                },
                {
                    "id": "endTime",
                    "type": "Timestamp"
                }
                ]
            },
            "records": {
                "datasetDescription": "三十六小時天氣預報",
                "location": [
                {
                    "locationName": "宜蘭縣",
                    "weatherElement": [
                    {
                        "elementName": "Wx",
                        "time": [
                        {
                            "startTime": "2023-08-26 12:00:00",
                            "endTime": "2023-08-26 18:00:00",
                            "parameter": {
                            "parameterName": "多雲",
                            "parameterValue": "4"
                            }
                        },
                        {
                            "startTime": "2023-08-26 18:00:00",
                            "endTime": "2023-08-27 06:00:00",
                            "parameter": {
                            "parameterName": "晴時多雲",
                            "parameterValue": "2"
                            }
                        },
                        {
                            "startTime": "2023-08-27 06:00:00",
                            "endTime": "2023-08-27 18:00:00",
                            "parameter": {
                            "parameterName": "晴時多雲",
                            "parameterValue": "2"
                            }
                        }
                        ]
                    },
                    {
                        "elementName": "PoP",
                        "time": [
                        {
                            "startTime": "2023-08-26 12:00:00",
                            "endTime": "2023-08-26 18:00:00",
                            "parameter": {
                            "parameterName": "20",
                            "parameterUnit": "百分比"
                            }
                        },
                        {
                            "startTime": "2023-08-26 18:00:00",
                            "endTime": "2023-08-27 06:00:00",
                            "parameter": {
                            "parameterName": "10",
                            "parameterUnit": "百分比"
                            }
                        },
                        {
                            "startTime": "2023-08-27 06:00:00",
                            "endTime": "2023-08-27 18:00:00",
                            "parameter": {
                            "parameterName": "10",
                            "parameterUnit": "百分比"
                            }
                        }
                        ]
                    },
                    {
                        "elementName": "MinT",
                        "time": [
                        {
                            "startTime": "2023-08-26 12:00:00",
                            "endTime": "2023-08-26 18:00:00",
                            "parameter": {
                            "parameterName": "29",
                            "parameterUnit": "C"
                            }
                        },
                        {
                            "startTime": "2023-08-26 18:00:00",
                            "endTime": "2023-08-27 06:00:00",
                            "parameter": {
                            "parameterName": "25",
                            "parameterUnit": "C"
                            }
                        },
                        {
                            "startTime": "2023-08-27 06:00:00",
                            "endTime": "2023-08-27 18:00:00",
                            "parameter": {
                            "parameterName": "25",
                            "parameterUnit": "C"
                            }
                        }
                        ]
                    },
                    {
                        "elementName": "MaxT",
                        "time": [
                        {
                            "startTime": "2023-08-26 12:00:00",
                            "endTime": "2023-08-26 18:00:00",
                            "parameter": {
                            "parameterName": "32",
                            "parameterUnit": "C"
                            }
                        },
                        {
                            "startTime": "2023-08-26 18:00:00",
                            "endTime": "2023-08-27 06:00:00",
                            "parameter": {
                            "parameterName": "29",
                            "parameterUnit": "C"
                            }
                        },
                        {
                            "startTime": "2023-08-27 06:00:00",
                            "endTime": "2023-08-27 18:00:00",
                            "parameter": {
                            "parameterName": "32",
                            "parameterUnit": "C"
                            }
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            }

@pytest.fixture()
def test_data_split():
    return ([{'elementName': 'Wx', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '多雲', 'parameterValue': '4'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '晴時多雲', 'parameterValue': '2'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '晴時多雲', 'parameterValue': '2'}}]}], [{'elementName': 'PoP', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '20', 'parameterUnit': '百分比'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '10', 'parameterUnit': '百分比'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '10', 'parameterUnit': '百分比'}}]}], [{'elementName': 'MinT', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '29', 'parameterUnit': 'C'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '25', 'parameterUnit': 'C'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '25', 'parameterUnit': 'C'}}]}], [{'elementName': 'MaxT', 'time': [{'startTime': '2023-08-26 12:00:00', 'endTime': '2023-08-26 18:00:00', 'parameter': {'parameterName': '32', 'parameterUnit': 'C'}}, {'startTime': '2023-08-26 18:00:00', 'endTime': '2023-08-27 06:00:00', 'parameter': {'parameterName': '29', 'parameterUnit': 'C'}}, {'startTime': '2023-08-27 06:00:00', 'endTime': '2023-08-27 18:00:00', 'parameter': {'parameterName': '32', 'parameterUnit': 'C'}}]}])

@pytest.fixture()
def test_weather_split():
    return (['2023-08-26 12:00:00', '2023-08-26 18:00:00', '2023-08-27 06:00:00'], ['2023-08-26 18:00:00', '2023-08-27 06:00:00', '2023-08-27 18:00:00'])