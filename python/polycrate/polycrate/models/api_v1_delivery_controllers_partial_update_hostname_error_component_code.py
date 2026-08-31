from typing import Literal

ApiV1DeliveryControllersPartialUpdateHostnameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersPartialUpdateHostnameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_delivery_controllers_partial_update_hostname_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersPartialUpdateHostnameErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_PARTIAL_UPDATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
