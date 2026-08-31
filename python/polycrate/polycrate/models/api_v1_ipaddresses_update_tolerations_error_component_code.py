from typing import Literal

ApiV1IpaddressesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_IPADDRESSES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_ipaddresses_update_tolerations_error_component_code(
    value: str,
) -> ApiV1IpaddressesUpdateTolerationsErrorComponentCode:
    if value in API_V1_IPADDRESSES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
