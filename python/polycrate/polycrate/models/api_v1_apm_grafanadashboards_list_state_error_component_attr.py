from typing import Literal

ApiV1ApmGrafanadashboardsListStateErrorComponentAttr = Literal["state"]

API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_apm_grafanadashboards_list_state_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsListStateErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
