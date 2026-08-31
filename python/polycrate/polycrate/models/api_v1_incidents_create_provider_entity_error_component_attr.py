from typing import Literal

ApiV1IncidentsCreateProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_INCIDENTS_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsCreateProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_incidents_create_provider_entity_error_component_attr(
    value: str,
) -> ApiV1IncidentsCreateProviderEntityErrorComponentAttr:
    if value in API_V1_INCIDENTS_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
