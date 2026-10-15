from typing import Literal

K8SAddonConfigRevisionRequestScope = Literal["system", "user"]

K8S_ADDON_CONFIG_REVISION_REQUEST_SCOPE_VALUES: set[K8SAddonConfigRevisionRequestScope] = {
    "system",
    "user",
}


def check_k8s_addon_config_revision_request_scope(value: str) -> K8SAddonConfigRevisionRequestScope:
    if value in K8S_ADDON_CONFIG_REVISION_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_REQUEST_SCOPE_VALUES!r}")
