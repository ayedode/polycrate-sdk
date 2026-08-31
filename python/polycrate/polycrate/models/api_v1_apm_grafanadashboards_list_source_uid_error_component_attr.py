from typing import Literal

ApiV1ApmGrafanadashboardsListSourceUidErrorComponentAttr = Literal["source_uid"]

API_V1_APM_GRAFANADASHBOARDS_LIST_SOURCE_UID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsListSourceUidErrorComponentAttr
] = {
    "source_uid",
}


def check_api_v1_apm_grafanadashboards_list_source_uid_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsListSourceUidErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_SOURCE_UID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_SOURCE_UID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
