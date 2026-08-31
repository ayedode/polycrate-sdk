from typing import Literal

ApiV1KubernetesVolumesUpdatePvcNameErrorComponentAttr = Literal["pvc_name"]

API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdatePvcNameErrorComponentAttr
] = {
    "pvc_name",
}


def check_api_v1_kubernetes_volumes_update_pvc_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdatePvcNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
