from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListScope = Literal["system", "user"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SCOPE_VALUES: set[ApiV1KubernetesAddonConfigRevisionsListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_addon_config_revisions_list_scope(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListScope:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_SCOPE_VALUES!r}"
    )
