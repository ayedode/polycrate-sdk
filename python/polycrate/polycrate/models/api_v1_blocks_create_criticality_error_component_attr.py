from typing import Literal

ApiV1BlocksCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_blocks_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
