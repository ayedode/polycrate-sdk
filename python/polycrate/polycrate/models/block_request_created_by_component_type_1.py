from typing import Literal

BlockRequestCreatedByComponentType1 = Literal["", "api", "cli", "operator"]

BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES: set[BlockRequestCreatedByComponentType1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_block_request_created_by_component_type_1(value: str) -> BlockRequestCreatedByComponentType1:
    if value in BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_1_VALUES!r}")
