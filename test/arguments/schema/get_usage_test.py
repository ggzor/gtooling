import pytest
from utils.arguments.schema import ArgsSchema, RequiredArg, OptionalArg

params = [
    (ArgsSchema("test", "", []), "test"),

    (ArgsSchema("test", "", [
        RequiredArg("req1")
    ]), "test req1"),

    (ArgsSchema("test", "", [
        RequiredArg("req1"), OptionalArg("opt1", 0)
    ]), "test req1 [opt1=0]"),

    (ArgsSchema("test", "", [
        OptionalArg("opt1", []), OptionalArg("opt2", 0) 
    ]), "test [opt1=[]] [opt2=0]")
]

@pytest.mark.parametrize("schema, expected", params)
def test_shouldBe_expected_when_noArgs_and_schemaIs(schema, expected):
    assert expected == schema.get_usage()