from typing import Literal

ApiV1DeliveryControllersUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersUpdateDebugModeErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
