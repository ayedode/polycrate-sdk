from typing import Literal

ApiV1AlertsUpdateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ALERTS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[ApiV1AlertsUpdateBlockErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_alerts_update_block_error_component_code(value: str) -> ApiV1AlertsUpdateBlockErrorComponentCode:
    if value in API_V1_ALERTS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_UPDATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
