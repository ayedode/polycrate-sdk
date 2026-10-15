from typing import Literal

K8SAddonConfigRevisionScope = Literal["system", "user"]

K8S_ADDON_CONFIG_REVISION_SCOPE_VALUES: set[K8SAddonConfigRevisionScope] = {
    "system",
    "user",
}


def check_k8s_addon_config_revision_scope(value: str) -> K8SAddonConfigRevisionScope:
    if value in K8S_ADDON_CONFIG_REVISION_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {K8S_ADDON_CONFIG_REVISION_SCOPE_VALUES!r}")
