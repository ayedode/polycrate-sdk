from typing import Literal

ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_kubernetes_volumes_archive_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateProviderIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
