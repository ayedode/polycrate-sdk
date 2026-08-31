from typing import Literal

ApiV1DatasourcesListProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_DATASOURCES_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesListProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_datasources_list_provider_entity_error_component_attr(
    value: str,
) -> ApiV1DatasourcesListProviderEntityErrorComponentAttr:
    if value in API_V1_DATASOURCES_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_LIST_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
