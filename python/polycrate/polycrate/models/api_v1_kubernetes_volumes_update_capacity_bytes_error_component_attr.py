from typing import Literal

ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponentAttr = Literal["capacity_bytes"]

API_V1_KUBERNETES_VOLUMES_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponentAttr
] = {
    "capacity_bytes",
}


def check_api_v1_kubernetes_volumes_update_capacity_bytes_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateCapacityBytesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
