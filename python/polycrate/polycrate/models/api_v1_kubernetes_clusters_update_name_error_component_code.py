from typing import Literal

ApiV1KubernetesClustersUpdateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersUpdateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_update_name_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersUpdateNameErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
