from typing import Literal

K8SAddonConfigRevisionKind = Literal["generic"]

K8S_ADDON_CONFIG_REVISION_KIND_VALUES: set[K8SAddonConfigRevisionKind] = {
    "generic",
}


def check_k8s_addon_config_revision_kind(value: str) -> K8SAddonConfigRevisionKind:
    if value in K8S_ADDON_CONFIG_REVISION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_KIND_VALUES!r}")
