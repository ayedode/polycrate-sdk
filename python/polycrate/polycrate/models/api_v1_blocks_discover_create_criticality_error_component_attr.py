from typing import Literal

ApiV1BlocksDiscoverCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_discover_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
