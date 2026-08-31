from typing import Literal

ApiV1KubernetesVolumesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_VOLUMES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_volumes_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
