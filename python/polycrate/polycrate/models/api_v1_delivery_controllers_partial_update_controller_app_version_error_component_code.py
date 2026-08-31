from typing import Literal

ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_delivery_controllers_partial_update_controller_app_version_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateControllerAppVersionErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_CONTROLLER_APP_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
