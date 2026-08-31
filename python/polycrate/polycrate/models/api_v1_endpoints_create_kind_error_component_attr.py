from typing import Literal

ApiV1EndpointsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_ENDPOINTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_endpoints_create_kind_error_component_attr(value: str) -> ApiV1EndpointsCreateKindErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
