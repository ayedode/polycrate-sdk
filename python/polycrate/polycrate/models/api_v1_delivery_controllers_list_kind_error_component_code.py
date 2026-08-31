from typing import Literal

ApiV1DeliveryControllersListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_DELIVERY_CONTROLLERS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersListKindErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_delivery_controllers_list_kind_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersListKindErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
