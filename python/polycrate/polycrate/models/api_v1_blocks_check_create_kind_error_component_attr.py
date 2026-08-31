from typing import Literal

ApiV1BlocksCheckCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCKS_CHECK_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCheckCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_blocks_check_create_kind_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateKindErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
