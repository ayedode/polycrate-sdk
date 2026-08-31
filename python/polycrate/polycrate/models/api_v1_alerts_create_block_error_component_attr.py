from typing import Literal

ApiV1AlertsCreateBlockErrorComponentAttr = Literal["block"]

API_V1_ALERTS_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsCreateBlockErrorComponentAttr] = {
    "block",
}


def check_api_v1_alerts_create_block_error_component_attr(value: str) -> ApiV1AlertsCreateBlockErrorComponentAttr:
    if value in API_V1_ALERTS_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_CREATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
