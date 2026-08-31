from typing import Literal

ApiV1HostsPartialUpdateSloTargetErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_HOSTS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsPartialUpdateSloTargetErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_hosts_partial_update_slo_target_error_component_code(
    value: str,
) -> ApiV1HostsPartialUpdateSloTargetErrorComponentCode:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_SLO_TARGET_ERROR_COMPONENT_CODE_VALUES!r}"
    )
