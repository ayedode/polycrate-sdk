from typing import Literal

ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponentAttr = Literal["csi_driver"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponentAttr
] = {
    "csi_driver",
}


def check_api_v1_kubernetes_volumes_partial_update_csi_driver_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateCsiDriverErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
