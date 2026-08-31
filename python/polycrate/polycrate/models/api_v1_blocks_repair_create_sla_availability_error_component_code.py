from typing import Literal

ApiV1BlocksRepairCreateSlaAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_BLOCKS_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateSlaAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_blocks_repair_create_sla_availability_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateSlaAvailabilityErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
