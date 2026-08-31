from typing import Literal

ApiV1IncidentsUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_INCIDENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_incidents_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateProviderIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
