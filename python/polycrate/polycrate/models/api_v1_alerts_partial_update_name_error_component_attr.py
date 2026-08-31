from typing import Literal

ApiV1AlertsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_ALERTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsPartialUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_alerts_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1AlertsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_ALERTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
