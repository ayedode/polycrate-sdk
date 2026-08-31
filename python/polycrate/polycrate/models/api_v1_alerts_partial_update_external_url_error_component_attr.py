from typing import Literal

ApiV1AlertsPartialUpdateExternalUrlErrorComponentAttr = Literal["external_url"]

API_V1_ALERTS_PARTIAL_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsPartialUpdateExternalUrlErrorComponentAttr
] = {
    "external_url",
}


def check_api_v1_alerts_partial_update_external_url_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateExternalUrlErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_EXTERNAL_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
