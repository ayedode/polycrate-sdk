from typing import Literal

ApiV1EndpointsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ENDPOINTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_endpoints_update_criticality_error_component_attr(
    value: str,
) -> ApiV1EndpointsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
