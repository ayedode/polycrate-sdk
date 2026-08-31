from typing import Literal

ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponentAttr = Literal["k8s_app"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponentAttr
] = {
    "k8s_app",
}


def check_api_v1_registry_registries_archive_create_k8s_app_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateK8SAppErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_K8S_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
