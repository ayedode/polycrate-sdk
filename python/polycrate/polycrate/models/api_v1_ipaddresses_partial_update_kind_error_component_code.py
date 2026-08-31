from typing import Literal

ApiV1IpaddressesPartialUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IPADDRESSES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesPartialUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_ipaddresses_partial_update_kind_error_component_code(
    value: str,
) -> ApiV1IpaddressesPartialUpdateKindErrorComponentCode:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
