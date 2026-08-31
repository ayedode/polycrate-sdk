from typing import Literal

ApiV1RegistryRegistriesListKindErrorComponentAttr = Literal["kind"]

API_V1_REGISTRY_REGISTRIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_registry_registries_list_kind_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesListKindErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
