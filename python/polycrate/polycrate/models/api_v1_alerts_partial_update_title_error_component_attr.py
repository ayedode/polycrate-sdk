from typing import Literal

ApiV1AlertsPartialUpdateTitleErrorComponentAttr = Literal["title"]

API_V1_ALERTS_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsPartialUpdateTitleErrorComponentAttr] = {
    "title",
}


def check_api_v1_alerts_partial_update_title_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateTitleErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
