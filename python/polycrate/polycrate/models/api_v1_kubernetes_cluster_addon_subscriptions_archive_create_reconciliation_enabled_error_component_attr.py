from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponentAttr = Literal[
    "reconciliation_enabled"
]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponentAttr
] = {
    "reconciliation_enabled",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_reconciliation_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateReconciliationEnabledErrorComponentAttr:
    if (
        value
        in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
