from typing import Literal

ApiV1KubernetesControlplanesCreateRegionIdErrorComponentAttr = Literal["region_id"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateRegionIdErrorComponentAttr
] = {
    "region_id",
}


def check_api_v1_kubernetes_controlplanes_create_region_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateRegionIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_REGION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
