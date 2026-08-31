from typing import Literal

ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponentAttr = Literal["cloud_provider_volume_id"]

API_V1_KUBERNETES_VOLUMES_LIST_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponentAttr
] = {
    "cloud_provider_volume_id",
}


def check_api_v1_kubernetes_volumes_list_cloud_provider_volume_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListCloudProviderVolumeIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
