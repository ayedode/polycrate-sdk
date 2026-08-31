from typing import Literal

ApiV1IncidentsUpdateProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_INCIDENTS_UPDATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_incidents_update_provider_entity_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateProviderEntityErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
