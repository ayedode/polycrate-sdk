from typing import Literal

ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_IPADDRESSES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_ipaddresses_partial_update_sla_availability_error_component_code(
    value: str,
) -> ApiV1IpaddressesPartialUpdateSlaAvailabilityErrorComponentCode:
    if value in API_V1_IPADDRESSES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
