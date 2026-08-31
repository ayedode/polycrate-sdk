from typing import Literal

ApiV1KubernetesClustersPartialUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersPartialUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_partial_update_name_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersPartialUpdateNameErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
