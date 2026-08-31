from typing import Literal

ApiV1AlertsUpdateExternalUrlErrorComponentAttr = Literal["external_url"]

API_V1_ALERTS_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateExternalUrlErrorComponentAttr] = {
    "external_url",
}


def check_api_v1_alerts_update_external_url_error_component_attr(
    value: str,
) -> ApiV1AlertsUpdateExternalUrlErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
