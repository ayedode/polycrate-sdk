from typing import Literal

ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponentCode = Literal[
    "date", "invalid", "make_aware", "null", "overflow"
]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_FINISHED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "null",
    "overflow",
}


def check_api_v1_cli_activities_partial_update_finished_at_error_component_code(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponentCode:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_FINISHED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_FINISHED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
