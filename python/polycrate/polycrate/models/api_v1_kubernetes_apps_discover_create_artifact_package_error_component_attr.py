from typing import Literal

ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_api_v1_kubernetes_apps_discover_create_artifact_package_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateArtifactPackageErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
