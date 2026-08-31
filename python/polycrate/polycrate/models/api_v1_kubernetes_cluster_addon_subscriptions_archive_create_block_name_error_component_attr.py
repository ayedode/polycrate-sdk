from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_archive_create_block_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsArchiveCreateBlockNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_ARCHIVE_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
