from typing import Literal

K8SAddonConfigRevisionRequestKind = Literal["generic"]

K8S_ADDON_CONFIG_REVISION_REQUEST_KIND_VALUES: set[K8SAddonConfigRevisionRequestKind] = {
    "generic",
}


def check_k8s_addon_config_revision_request_kind(value: str) -> K8SAddonConfigRevisionRequestKind:
    if value in K8S_ADDON_CONFIG_REVISION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_REQUEST_KIND_VALUES!r}")
