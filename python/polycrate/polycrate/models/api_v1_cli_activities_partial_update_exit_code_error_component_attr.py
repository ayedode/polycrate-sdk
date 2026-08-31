from typing import Literal

ApiV1CliActivitiesPartialUpdateExitCodeErrorComponentAttr = Literal["exit_code"]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_EXIT_CODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CliActivitiesPartialUpdateExitCodeErrorComponentAttr
] = {
    "exit_code",
}


def check_api_v1_cli_activities_partial_update_exit_code_error_component_attr(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateExitCodeErrorComponentAttr:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_EXIT_CODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_EXIT_CODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
