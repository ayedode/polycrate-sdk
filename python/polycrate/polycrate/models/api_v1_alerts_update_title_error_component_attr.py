from typing import Literal

ApiV1AlertsUpdateTitleErrorComponentAttr = Literal["title"]

API_V1_ALERTS_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateTitleErrorComponentAttr] = {
    "title",
}


def check_api_v1_alerts_update_title_error_component_attr(value: str) -> ApiV1AlertsUpdateTitleErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
