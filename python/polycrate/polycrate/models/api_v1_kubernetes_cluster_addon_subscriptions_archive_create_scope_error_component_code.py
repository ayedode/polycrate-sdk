from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_scope_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateScopeErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
