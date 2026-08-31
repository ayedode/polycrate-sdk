from typing import Literal

ApiV1IncidentsCreateReporterErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_INCIDENTS_CREATE_REPORTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1IncidentsCreateReporterErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_incidents_create_reporter_error_component_code(
    value: str,
) -> ApiV1IncidentsCreateReporterErrorComponentCode:
    if value in API_V1_INCIDENTS_CREATE_REPORTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_REPORTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
