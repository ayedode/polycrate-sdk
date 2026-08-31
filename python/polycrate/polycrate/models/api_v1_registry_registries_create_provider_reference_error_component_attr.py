from typing import Literal

ApiV1RegistryRegistriesCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_registry_registries_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
