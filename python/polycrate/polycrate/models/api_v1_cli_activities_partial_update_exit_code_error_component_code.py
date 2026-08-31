from typing import Literal

ApiV1CliActivitiesPartialUpdateExitCodeErrorComponentCode = Literal["invalid", "max_string_length", "null"]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_EXIT_CODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CliActivitiesPartialUpdateExitCodeErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "null",
}


def check_api_v1_cli_activities_partial_update_exit_code_error_component_code(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateExitCodeErrorComponentCode:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_EXIT_CODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_EXIT_CODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
