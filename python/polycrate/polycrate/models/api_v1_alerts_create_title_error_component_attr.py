from typing import Literal

ApiV1AlertsCreateTitleErrorComponentAttr = Literal["title"]

API_V1_ALERTS_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateTitleErrorComponentAttr] = {
    "title",
}


def check_api_v1_alerts_create_title_error_component_attr(value: str) -> ApiV1AlertsCreateTitleErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_TITLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
