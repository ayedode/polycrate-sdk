from typing import Literal

ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_delivery_controllers_update_applications_degraded_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersUpdateApplicationsDegradedErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_APPLICATIONS_DEGRADED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
