from typing import Literal

ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_cluster_addon_subscriptions_update_block_name_error_component_code(
    value: str,
) -> ApiV1KubernetesClusterAddonSubscriptionsUpdateBlockNameErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTER_ADDON_SUBSCRIPTIONS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
