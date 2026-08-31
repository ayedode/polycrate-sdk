from typing import Literal

ApiV1IpaddressesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_IPADDRESSES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IpaddressesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_ipaddresses_update_kind_error_component_code(
    value: str,
) -> ApiV1IpaddressesUpdateKindErrorComponentCode:
    if value in API_V1_IPADDRESSES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
