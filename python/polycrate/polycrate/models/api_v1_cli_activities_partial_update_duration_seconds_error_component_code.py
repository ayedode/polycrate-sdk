from typing import Literal

ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponentCode = Literal[
    "invalid", "max_string_length", "min_value", "null"
]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "min_value",
    "null",
}


def check_api_v1_cli_activities_partial_update_duration_seconds_error_component_code(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponentCode:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_DURATION_SECONDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
