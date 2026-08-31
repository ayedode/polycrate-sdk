from typing import Literal

ApiV1PopsUpdateProviderEntityIdErrorComponentAttr = Literal["provider_entity_id"]

API_V1_POPS_UPDATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsUpdateProviderEntityIdErrorComponentAttr
] = {
    "provider_entity_id",
}


def check_api_v1_pops_update_provider_entity_id_error_component_attr(
    value: str,
) -> ApiV1PopsUpdateProviderEntityIdErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_PROVIDER_ENTITY_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
