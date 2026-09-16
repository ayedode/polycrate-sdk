from typing import Literal

ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponentAttr = Literal["exposure_type"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponentAttr
] = {
    "exposure_type",
}


def check_api_v1_kubernetes_controlplanes_update_exposure_type_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_EXPOSURE_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
