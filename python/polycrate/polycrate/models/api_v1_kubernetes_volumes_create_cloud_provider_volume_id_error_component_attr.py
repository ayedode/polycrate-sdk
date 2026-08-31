from typing import Literal

ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponentAttr = Literal["cloud_provider_volume_id"]

API_V1_KUBERNETES_VOLUMES_CREATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponentAttr
] = {
    "cloud_provider_volume_id",
}


def check_api_v1_kubernetes_volumes_create_cloud_provider_volume_id_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreateCloudProviderVolumeIdErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_CLOUD_PROVIDER_VOLUME_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
