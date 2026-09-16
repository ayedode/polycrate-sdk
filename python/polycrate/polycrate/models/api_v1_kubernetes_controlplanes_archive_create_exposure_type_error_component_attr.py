from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateExposureTypeErrorComponentAttr = Literal["exposure_type"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_EXPOSURE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateExposureTypeErrorComponentAttr
] = {
    "exposure_type",
}


def check_api_v1_kubernetes_controlplanes_archive_create_exposure_type_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateExposureTypeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_EXPOSURE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_EXPOSURE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
