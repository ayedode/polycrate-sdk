from typing import Literal

ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponentAttr = Literal["capacity_bytes"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponentAttr
] = {
    "capacity_bytes",
}


def check_api_v1_kubernetes_volumes_partial_update_capacity_bytes_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdateCapacityBytesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_CAPACITY_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
