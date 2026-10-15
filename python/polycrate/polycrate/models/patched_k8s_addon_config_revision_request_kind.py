from typing import Literal

PatchedK8SAddonConfigRevisionRequestKind = Literal["generic"]

PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_KIND_VALUES: set[PatchedK8SAddonConfigRevisionRequestKind] = {
    "generic",
}


def check_patched_k8s_addon_config_revision_request_kind(value: str) -> PatchedK8SAddonConfigRevisionRequestKind:
    if value in PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_K8S_ADDON_CONFIG_REVISION_REQUEST_KIND_VALUES!r}"
    )
