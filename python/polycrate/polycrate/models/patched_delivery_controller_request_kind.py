from typing import Literal

PatchedDeliveryControllerRequestKind = Literal["argocd", "flux", "generic"]

PATCHED_DELIVERY_CONTROLLER_REQUEST_KIND_VALUES: set[PatchedDeliveryControllerRequestKind] = {
    "argocd",
    "flux",
    "generic",
}


def check_patched_delivery_controller_request_kind(value: str) -> PatchedDeliveryControllerRequestKind:
    if value in PATCHED_DELIVERY_CONTROLLER_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_DELIVERY_CONTROLLER_REQUEST_KIND_VALUES!r}")
