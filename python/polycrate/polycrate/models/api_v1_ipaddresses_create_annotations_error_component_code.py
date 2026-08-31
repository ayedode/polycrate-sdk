from typing import Literal

ApiV1IpaddressesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_IPADDRESSES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_ipaddresses_create_annotations_error_component_code(
    value: str,
) -> ApiV1IpaddressesCreateAnnotationsErrorComponentCode:
    if value in API_V1_IPADDRESSES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
