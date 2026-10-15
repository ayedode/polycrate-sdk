from typing import Literal

PatchedK8SAddonConfigRevisionRequestScope = Literal["system", "user"]

PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_SCOPE_VALUES: set[PatchedK8SAddonConfigRevisionRequestScope] = {
    "system",
    "user",
}


def check_patched_k8s_addon_config_revision_request_scope(value: str) -> PatchedK8SAddonConfigRevisionRequestScope:
    if value in PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_SCOPE_VALUES!r}"
    )
