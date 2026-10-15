from typing import Literal

DeliveryControllerKind = Literal["argocd", "flux", "generic"]

DELIVERY_CONTROLLER_KIND_VALUES: set[DeliveryControllerKind] = {
    "argocd",
    "flux",
    "generic",
}


def check_delivery_controller_kind(value: str) -> DeliveryControllerKind:
    if value in DELIVERY_CONTROLLER_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_KIND_VALUES!r}")
