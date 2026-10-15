from typing import Literal

K8SAddonKind = Literal["generic"]

K8S_ADDON_KIND_VALUES: set[K8SAddonKind] = {
    "generic",
}


def check_k8s_addon_kind(value: str) -> K8SAddonKind:
    if value in K8S_ADDON_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_KIND_VALUES!r}")
