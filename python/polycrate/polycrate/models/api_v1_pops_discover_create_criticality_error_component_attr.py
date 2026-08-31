from typing import Literal

ApiV1PopsDiscoverCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_POPS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pops_discover_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateCriticalityErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
