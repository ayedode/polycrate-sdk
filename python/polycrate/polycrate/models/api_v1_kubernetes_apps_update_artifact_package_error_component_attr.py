from typing import Literal

ApiV1KubernetesAppsUpdateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

API_V1_KUBERNETES_APPS_UPDATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_api_v1_kubernetes_apps_update_artifact_package_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateArtifactPackageErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
