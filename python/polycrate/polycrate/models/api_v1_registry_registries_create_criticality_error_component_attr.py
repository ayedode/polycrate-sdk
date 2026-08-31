from typing import Literal

ApiV1RegistryRegistriesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_REGISTRY_REGISTRIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_registry_registries_create_criticality_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateCriticalityErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
