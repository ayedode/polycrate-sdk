from typing import Literal

ApiV1AlertsArchiveCreatePanelUrlErrorComponentAttr = Literal["panel_url"]

API_V1_ALERTS_ARCHIVE_CREATE_PANEL_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreatePanelUrlErrorComponentAttr
] = {
    "panel_url",
}


def check_api_v1_alerts_archive_create_panel_url_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreatePanelUrlErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_PANEL_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_PANEL_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
