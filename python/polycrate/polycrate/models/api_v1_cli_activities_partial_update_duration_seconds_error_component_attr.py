from typing import Literal

ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponentAttr = Literal["duration_seconds"]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponentAttr
] = {
    "duration_seconds",
}


def check_api_v1_cli_activities_partial_update_duration_seconds_error_component_attr(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponentAttr:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_DURATION_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
