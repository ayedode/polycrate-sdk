from typing import Literal

BlockRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[BlockRequestCreatedByComponentType3Type1] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_block_request_created_by_component_type_3_type_1(value: str) -> BlockRequestCreatedByComponentType3Type1:
    if value in BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
