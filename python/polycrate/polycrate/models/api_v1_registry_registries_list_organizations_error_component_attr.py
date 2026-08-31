from typing import Literal

ApiV1RegistryRegistriesListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_REGISTRY_REGISTRIES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_registry_registries_list_organizations_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesListOrganizationsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
