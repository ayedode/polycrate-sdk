from typing import Literal

ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponentAttr = Literal["provider_object_id"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponentAttr
] = {
    "provider_object_id",
}


def check_api_v1_kubernetes_volumes_archive_create_provider_object_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateProviderObjectIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
