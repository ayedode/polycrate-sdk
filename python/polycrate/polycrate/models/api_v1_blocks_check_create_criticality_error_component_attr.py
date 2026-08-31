from typing import Literal

ApiV1BlocksCheckCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_check_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
