from typing import Literal

ApiV1KubernetesClustersUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_kubernetes_clusters_update_description_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateDescriptionErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
