from typing import Literal

ApiV1DeliveryControllersCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DELIVERY_CONTROLLERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_delivery_controllers_create_kind_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersCreateKindErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
