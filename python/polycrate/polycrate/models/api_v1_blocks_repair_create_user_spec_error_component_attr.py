from typing import Literal

ApiV1BlocksRepairCreateUserSpecErrorComponentAttr = Literal["user_spec"]

API_V1_BLOCKS_REPAIR_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateUserSpecErrorComponentAttr
] = {
    "user_spec",
}


def check_api_v1_blocks_repair_create_user_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateUserSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
