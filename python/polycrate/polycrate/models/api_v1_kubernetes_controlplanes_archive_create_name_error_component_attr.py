from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_controlplanes_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
