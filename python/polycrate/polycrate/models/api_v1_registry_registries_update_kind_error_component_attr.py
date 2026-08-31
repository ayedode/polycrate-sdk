from typing import Literal

ApiV1RegistryRegistriesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_REGISTRY_REGISTRIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_registry_registries_update_kind_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateKindErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
