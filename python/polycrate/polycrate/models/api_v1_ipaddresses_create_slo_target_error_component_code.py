from typing import Literal

ApiV1IpaddressesCreateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_IPADDRESSES_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesCreateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_ipaddresses_create_slo_target_error_component_code(
    value: str,
) -> ApiV1IpaddressesCreateSloTargetErrorComponentCode:
    if value in API_V1_IPADDRESSES_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
