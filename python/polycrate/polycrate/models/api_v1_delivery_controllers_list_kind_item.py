from typing import Literal

ApiV1DeliveryControllersListKindItem = Literal["argocd", "flux", "generic"]

API_V1_DELIVERY_CONTROLLERS_LIST_KIND_ITEM_VALUES: set[ApiV1DeliveryControllersListKindItem] = {
    "argocd",
    "flux",
    "generic",
}


def check_api_v1_delivery_controllers_list_kind_item(value: str) -> ApiV1DeliveryControllersListKindItem:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_KIND_ITEM_VALUES!r}"
    )
