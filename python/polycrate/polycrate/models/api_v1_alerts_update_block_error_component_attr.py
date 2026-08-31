from typing import Literal

ApiV1AlertsUpdateBlockErrorComponentAttr = Literal["block"]

API_V1_ALERTS_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertsUpdateBlockErrorComponentAttr] = {
    "block",
}


def check_api_v1_alerts_update_block_error_component_attr(value: str) -> ApiV1AlertsUpdateBlockErrorComponentAttr:
    if value in API_V1_ALERTS_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
