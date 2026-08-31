from typing import Literal

ApiV1DeliveryControllersListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_DELIVERY_CONTROLLERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_delivery_controllers_list_state_not_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersListStateNotErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
