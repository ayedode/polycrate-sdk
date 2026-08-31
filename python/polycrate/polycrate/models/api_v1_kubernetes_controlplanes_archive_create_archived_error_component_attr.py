from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_controlplanes_archive_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
