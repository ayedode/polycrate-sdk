from typing import Literal

ApiV1RegistryRegistriesListKindItem = Literal["harbor"]

API_V1_REGISTRY_REGISTRIES_LIST_KIND_ITEM_VALUES: set[ApiV1RegistryRegistriesListKindItem] = {
    "harbor",
}


def check_api_v1_registry_registries_list_kind_item(value: str) -> ApiV1RegistryRegistriesListKindItem:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_KIND_ITEM_VALUES!r}")
