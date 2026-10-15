from typing import Literal

DeliveryControllerRequestKind = Literal["argocd", "flux", "generic"]

DELIVERY_CONTROLLER_REQUEST_KIND_VALUES: set[DeliveryControllerRequestKind] = {
    "argocd",
    "flux",
    "generic",
}


def check_delivery_controller_request_kind(value: str) -> DeliveryControllerRequestKind:
    if value in DELIVERY_CONTROLLER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_REQUEST_KIND_VALUES!r}")
