from typing import Literal

ApiV1DatasourcesUpdateSlaAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_DATASOURCES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DatasourcesUpdateSlaAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_datasources_update_sla_availability_error_component_code(
    value: str,
) -> ApiV1DatasourcesUpdateSlaAvailabilityErrorComponentCode:
    if value in API_V1_DATASOURCES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
