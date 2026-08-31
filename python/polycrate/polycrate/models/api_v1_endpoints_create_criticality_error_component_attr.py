from typing import Literal

ApiV1EndpointsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_ENDPOINTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_endpoints_create_criticality_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateCriticalityErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
