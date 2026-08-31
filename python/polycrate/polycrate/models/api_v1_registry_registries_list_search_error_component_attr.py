from typing import Literal

ApiV1RegistryRegistriesListSearchErrorComponentAttr = Literal["search"]

API_V1_REGISTRY_REGISTRIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_registry_registries_list_search_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesListSearchErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
