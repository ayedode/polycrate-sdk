from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_VALUES: set[ApiV1KubernetesAddonConfigRevisionsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_addon_config_revisions_list_state_not(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListStateNot:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_STATE_NOT_VALUES!r}"
    )
