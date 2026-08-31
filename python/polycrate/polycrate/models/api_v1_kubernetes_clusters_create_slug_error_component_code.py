from typing import Literal

ApiV1KubernetesClustersCreateSlugErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed", "unique"
]

API_V1_KUBERNETES_CLUSTERS_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateSlugErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_kubernetes_clusters_create_slug_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateSlugErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_SLUG_ERROR_COMPONENT_CODE_VALUES!r}"
    )
