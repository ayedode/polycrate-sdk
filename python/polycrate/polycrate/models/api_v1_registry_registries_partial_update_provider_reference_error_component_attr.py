from typing import Literal

ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_registry_registries_partial_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
