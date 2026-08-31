from typing import Literal

ApiV1AlertsUpdatePanelUrlErrorComponentAttr = Literal["panel_url"]

API_V1_ALERTS_UPDATE_PANEL_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdatePanelUrlErrorComponentAttr] = {
    "panel_url",
}


def check_api_v1_alerts_update_panel_url_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdatePanelUrlErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_PANEL_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_PANEL_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
