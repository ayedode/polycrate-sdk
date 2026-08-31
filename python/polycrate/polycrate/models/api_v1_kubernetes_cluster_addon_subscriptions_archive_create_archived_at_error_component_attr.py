from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
