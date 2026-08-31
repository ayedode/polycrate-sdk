from typing import Literal

ApiV1DeliveryControllersListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DELIVERY_CONTROLLERS_LIST_STATE_NOT_VALUES: set[ApiV1DeliveryControllersListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_delivery_controllers_list_state_not(value: str) -> ApiV1DeliveryControllersListStateNot:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_STATE_NOT_VALUES!r}"
    )
