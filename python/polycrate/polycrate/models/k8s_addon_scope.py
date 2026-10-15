from typing import Literal

K8SAddonScope = Literal["system", "user"]

K8S_ADDON_SCOPE_VALUES: set[K8SAddonScope] = {
    "system",
    "user",
}


def check_k8s_addon_scope(value: str) -> K8SAddonScope:
    if value in K8S_ADDON_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_SCOPE_VALUES!r}")
