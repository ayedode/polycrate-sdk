from typing import Literal

ApiV1KubernetesAppsUninstallCreateArtifactErrorComponentAttr = Literal["artifact"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateArtifactErrorComponentAttr
] = {
    "artifact",
}


def check_api_v1_kubernetes_apps_uninstall_create_artifact_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateArtifactErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
