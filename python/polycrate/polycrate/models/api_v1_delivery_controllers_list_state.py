from typing import Literal

ApiV1DeliveryControllersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DELIVERY_CONTROLLERS_LIST_STATE_VALUES: set[ApiV1DeliveryControllersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_delivery_controllers_list_state(value: str) -> ApiV1DeliveryControllersListState:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_STATE_VALUES!r}")
