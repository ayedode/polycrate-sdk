from typing import Literal

ApiV1ApmGrafanadashboardsListKindErrorComponentAttr = Literal["kind"]

API_V1_APM_GRAFANADASHBOARDS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_apm_grafanadashboards_list_kind_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsListKindErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
