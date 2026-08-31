from typing import Literal

DeliveryControllerKindEnum = Literal["argocd", "flux", "generic"]

DELIVERY_CONTROLLER_KIND_ENUM_VALUES: set[DeliveryControllerKindEnum] = {
    "argocd",
    "flux",
    "generic",
}


def check_delivery_controller_kind_enum(value: str) -> DeliveryControllerKindEnum:
    if value in DELIVERY_CONTROLLER_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELIVERY_CONTROLLER_KIND_ENUM_VALUES!r}")
