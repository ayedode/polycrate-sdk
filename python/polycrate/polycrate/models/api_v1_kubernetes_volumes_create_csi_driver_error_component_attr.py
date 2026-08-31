from typing import Literal

ApiV1KubernetesVolumesCreateCsiDriverErrorComponentAttr = Literal["csi_driver"]

API_V1_KUBERNETES_VOLUMES_CREATE_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateCsiDriverErrorComponentAttr
] = {
    "csi_driver",
}


def check_api_v1_kubernetes_volumes_create_csi_driver_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateCsiDriverErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
