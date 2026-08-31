from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_description_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateDescriptionErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
