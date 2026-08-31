from typing import Literal

ApiV1KubernetesVolumesCreatePvcNameErrorComponentAttr = Literal["pvc_name"]

API_V1_KUBERNETES_VOLUMES_CREATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreatePvcNameErrorComponentAttr
] = {
    "pvc_name",
}


def check_api_v1_kubernetes_volumes_create_pvc_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreatePvcNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_PVC_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
