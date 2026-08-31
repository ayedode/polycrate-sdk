from typing import Literal

ApiV1KubernetesAppsUpdateArtifactErrorComponentAttr = Literal["artifact"]

API_V1_KUBERNETES_APPS_UPDATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateArtifactErrorComponentAttr
] = {
    "artifact",
}


def check_api_v1_kubernetes_apps_update_artifact_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateArtifactErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
