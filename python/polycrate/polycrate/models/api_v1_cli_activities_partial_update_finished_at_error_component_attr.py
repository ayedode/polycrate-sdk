from typing import Literal

ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponentAttr = Literal["finished_at"]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_FINISHED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponentAttr
] = {
    "finished_at",
}


def check_api_v1_cli_activities_partial_update_finished_at_error_component_attr(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponentAttr:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_FINISHED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_FINISHED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
