import json

from main import Entity


def test_solution_serialization(json_content):
    json_data = json.loads(json_content)
    json_file_hierarchy = Entity.from_jsonable(json_data)

    assert json_file_hierarchy.devices[0].id == 123
    assert json_file_hierarchy.devices[0].alias == "Device123"
    assert json_file_hierarchy.devices[0].status == "on"
    assert json_file_hierarchy.devices[0].ip == "123.123.123.123"
    assert json_file_hierarchy.devices[1].id == 321
    assert json_file_hierarchy.devices[1].alias == "Device321"
    assert json_file_hierarchy.devices[1].status == "off"
    assert json_file_hierarchy.devices[1].ip == "321.32.15.179"


def test_solution_deserialization(json_content):
    json_data = json.loads(json_content)
    json_file_hierarchy = Entity.from_jsonable(json_data)
    serialized_data = json.dumps(json_file_hierarchy.to_jsonable(), indent=4)

    assert json.loads(serialized_data) == json_data
