from typing import Literal

ApiV1ApmGrafanadashboardsListKindItem = Literal["generic"]

API_V1_APM_GRAFANADASHBOARDS_LIST_KIND_ITEM_VALUES: set[ApiV1ApmGrafanadashboardsListKindItem] = {
    "generic",
}


def check_api_v1_apm_grafanadashboards_list_kind_item(value: str) -> ApiV1ApmGrafanadashboardsListKindItem:
    if value in API_V1_APM_GRAFANADASHBOARDS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_LIST_KIND_ITEM_VALUES!r}"
    )
