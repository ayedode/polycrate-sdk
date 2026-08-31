from typing import Literal

ApiV1ApmGrafanadashboardsListSourceUidErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_APM_GRAFANADASHBOARDS_LIST_SOURCE_UID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmGrafanadashboardsListSourceUidErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_apm_grafanadashboards_list_source_uid_error_component_code(
    value: str,
) -> ApiV1ApmGrafanadashboardsListSourceUidErrorComponentCode:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_SOURCE_UID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_SOURCE_UID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
