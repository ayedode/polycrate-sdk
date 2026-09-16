from typing import Literal

ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_update_exposure_type_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
