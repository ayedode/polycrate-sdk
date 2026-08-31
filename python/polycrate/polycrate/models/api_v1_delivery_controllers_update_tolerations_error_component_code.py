from typing import Literal

ApiV1DeliveryControllersUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_DELIVERY_CONTROLLERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_delivery_controllers_update_tolerations_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersUpdateTolerationsErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
