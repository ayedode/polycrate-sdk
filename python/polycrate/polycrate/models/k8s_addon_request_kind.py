from typing import Literal

K8SAddonRequestKind = Literal["generic"]

K8S_ADDON_REQUEST_KIND_VALUES: set[K8SAddonRequestKind] = {
    "generic",
}


def check_k8s_addon_request_kind(value: str) -> K8SAddonRequestKind:
    if value in K8S_ADDON_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_REQUEST_KIND_VALUES!r}")
