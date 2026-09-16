from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_partial_update_exposure_type_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
