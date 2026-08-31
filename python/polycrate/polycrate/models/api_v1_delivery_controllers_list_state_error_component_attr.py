from typing import Literal

ApiV1DeliveryControllersListStateErrorComponentAttr = Literal["state"]

API_V1_DELIVERY_CONTROLLERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_delivery_controllers_list_state_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersListStateErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
