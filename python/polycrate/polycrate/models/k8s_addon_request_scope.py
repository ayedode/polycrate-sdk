from typing import Literal

K8SAddonRequestScope = Literal["system", "user"]

K8S_ADDON_REQUEST_SCOPE_VALUES: set[K8SAddonRequestScope] = {
    "system",
    "user",
}


def check_k8s_addon_request_scope(value: str) -> K8SAddonRequestScope:
    if value in K8S_ADDON_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_REQUEST_SCOPE_VALUES!r}")
