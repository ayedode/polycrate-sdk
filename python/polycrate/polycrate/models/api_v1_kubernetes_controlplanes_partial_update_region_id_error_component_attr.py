from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponentAttr = Literal["region_id"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponentAttr
] = {
    "region_id",
}


def check_api_v1_kubernetes_controlplanes_partial_update_region_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
