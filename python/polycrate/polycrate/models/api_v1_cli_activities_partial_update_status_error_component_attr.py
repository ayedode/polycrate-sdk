from typing import Literal

ApiV1CliActivitiesPartialUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CliActivitiesPartialUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_cli_activities_partial_update_status_error_component_attr(
    value: str,
) -> ApiV1CliActivitiesPartialUpdateStatusErrorComponentAttr:
    if value in API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CLI_ACTIVITIES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
