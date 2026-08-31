from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_kubernetes_controlplanes_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
