from typing import Literal

ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponentAttr = Literal["artifact_package"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponentAttr
] = {
    "artifact_package",
}


def check_api_v1_kubernetes_apps_archive_create_artifact_package_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateArtifactPackageErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARTIFACT_PACKAGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
