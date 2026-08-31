from typing import Literal

ApiV1ApmGrafanadashboardsListSearchErrorComponentAttr = Literal["search"]

API_V1_APM_GRAFANADASHBOARDS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_apm_grafanadashboards_list_search_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsListSearchErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
