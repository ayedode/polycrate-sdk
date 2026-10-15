from typing import Literal

BlockCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

BLOCK_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[BlockCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_block_created_by_component_type_3_type_1(value: str) -> BlockCreatedByComponentType3Type1:
    if value in BLOCK_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}")
