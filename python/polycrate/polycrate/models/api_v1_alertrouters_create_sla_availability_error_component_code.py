from typing import Literal

ApiV1AlertroutersCreateSlaAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_ALERTROUTERS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersCreateSlaAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_alertrouters_create_sla_availability_error_component_code(
    value: str,
) -> ApiV1AlertroutersCreateSlaAvailabilityErrorComponentCode:
    if value in API_V1_ALERTROUTERS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
