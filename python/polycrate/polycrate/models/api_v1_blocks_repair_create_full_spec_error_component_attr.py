from typing import Literal

ApiV1BlocksRepairCreateFullSpecErrorComponentAttr = Literal["full_spec"]

API_V1_BLOCKS_REPAIR_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateFullSpecErrorComponentAttr
] = {
    "full_spec",
}


def check_api_v1_blocks_repair_create_full_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateFullSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_FULL_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
