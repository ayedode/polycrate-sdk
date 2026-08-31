from typing import Literal

ApiV1DeliveryControllersListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_DELIVERY_CONTROLLERS_LIST_TIME_RANGE_VALUES: set[ApiV1DeliveryControllersListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_delivery_controllers_list_time_range(value: str) -> ApiV1DeliveryControllersListTimeRange:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_TIME_RANGE_VALUES!r}"
    )
