from typing import Literal

ApiV1WorkspacesCreateActualAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_WORKSPACES_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCreateActualAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_workspaces_create_actual_availability_error_component_code(
    value: str,
) -> ApiV1WorkspacesCreateActualAvailabilityErrorComponentCode:
    if value in API_V1_WORKSPACES_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
