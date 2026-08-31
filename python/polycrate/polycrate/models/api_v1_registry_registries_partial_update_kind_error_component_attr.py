from typing import Literal

ApiV1RegistryRegistriesPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_registry_registries_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateKindErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
