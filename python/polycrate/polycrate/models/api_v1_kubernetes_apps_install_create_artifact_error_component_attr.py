from typing import Literal

ApiV1KubernetesAppsInstallCreateArtifactErrorComponentAttr = Literal["artifact"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateArtifactErrorComponentAttr
] = {
    "artifact",
}


def check_api_v1_kubernetes_apps_install_create_artifact_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateArtifactErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
