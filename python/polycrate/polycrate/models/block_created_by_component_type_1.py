from typing import Literal

BlockCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

BLOCK_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[BlockCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_block_created_by_component_type_1(value: str) -> BlockCreatedByComponentType1:
    if value in BLOCK_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}")
