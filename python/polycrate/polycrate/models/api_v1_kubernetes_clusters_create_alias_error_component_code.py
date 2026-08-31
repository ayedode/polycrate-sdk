from typing import Literal

ApiV1KubernetesClustersCreateAliasErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateAliasErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_create_alias_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateAliasErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
