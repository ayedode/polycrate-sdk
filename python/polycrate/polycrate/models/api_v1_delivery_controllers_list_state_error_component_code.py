from typing import Literal

ApiV1DeliveryControllersListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_DELIVERY_CONTROLLERS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DeliveryControllersListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_delivery_controllers_list_state_error_component_code(
    value: str,
) -> ApiV1DeliveryControllersListStateErrorComponentCode:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
