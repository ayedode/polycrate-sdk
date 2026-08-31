from typing import Literal

ApiV1AlertsArchiveCreateDashboardUrlErrorComponentAttr = Literal["dashboard_url"]

API_V1_ALERTS_ARCHIVE_CREATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateDashboardUrlErrorComponentAttr
] = {
    "dashboard_url",
}


def check_api_v1_alerts_archive_create_dashboard_url_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateDashboardUrlErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_DASHBOARD_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
