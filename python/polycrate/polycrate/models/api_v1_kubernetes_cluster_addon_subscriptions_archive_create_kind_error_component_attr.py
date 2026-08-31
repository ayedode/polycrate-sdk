from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
