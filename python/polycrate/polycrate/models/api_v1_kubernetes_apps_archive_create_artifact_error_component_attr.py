from typing import Literal

ApiV1KubernetesAppsArchiveCreateArtifactErrorComponentAttr = Literal["artifact"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateArtifactErrorComponentAttr
] = {
    "artifact",
}


def check_api_v1_kubernetes_apps_archive_create_artifact_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateArtifactErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARTIFACT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
