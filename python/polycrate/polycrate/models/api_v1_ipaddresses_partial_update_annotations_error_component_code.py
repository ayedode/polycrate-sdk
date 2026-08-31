from typing import Literal

ApiV1IpaddressesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_ipaddresses_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1IpaddressesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
