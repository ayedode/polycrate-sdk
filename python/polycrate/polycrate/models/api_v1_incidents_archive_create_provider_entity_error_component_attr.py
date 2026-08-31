from typing import Literal

ApiV1IncidentsArchiveCreateProviderEntityErrorComponentAttr = Literal["provider_entity"]

API_V1_INCIDENTS_ARCHIVE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateProviderEntityErrorComponentAttr
] = {
    "provider_entity",
}


def check_api_v1_incidents_archive_create_provider_entity_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateProviderEntityErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_PROVIDER_ENTITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
