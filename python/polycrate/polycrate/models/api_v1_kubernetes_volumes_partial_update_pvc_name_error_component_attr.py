from typing import Literal

ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponentAttr = Literal["pvc_name"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponentAttr
] = {
    "pvc_name",
}


def check_api_v1_kubernetes_volumes_partial_update_pvc_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdatePvcNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
