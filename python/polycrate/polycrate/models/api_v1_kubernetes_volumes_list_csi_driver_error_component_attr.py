from typing import Literal

ApiV1KubernetesVolumesListCsiDriverErrorComponentAttr = Literal["csi_driver"]

API_V1_KUBERNETES_VOLUMES_LIST_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListCsiDriverErrorComponentAttr
] = {
    "csi_driver",
}


def check_api_v1_kubernetes_volumes_list_csi_driver_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListCsiDriverErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_CSI_DRIVER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
