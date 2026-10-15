from typing import Literal

PatchedBlockRequestCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

PATCHED_BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    PatchedBlockRequestCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_patched_block_request_created_by_component_type_3_type_1(
    value: str,
) -> PatchedBlockRequestCreatedByComponentType3Type1:
    if value in PATCHED_BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_REQUEST_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
