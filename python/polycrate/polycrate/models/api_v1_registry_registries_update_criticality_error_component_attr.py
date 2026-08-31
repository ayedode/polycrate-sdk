from typing import Literal

ApiV1RegistryRegistriesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_REGISTRY_REGISTRIES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_registry_registries_update_criticality_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
