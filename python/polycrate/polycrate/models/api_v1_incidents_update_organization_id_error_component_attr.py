from typing import Literal

ApiV1IncidentsUpdateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_INCIDENTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsUpdateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_incidents_update_organization_id_error_component_attr(
    value: str,
) -> ApiV1IncidentsUpdateOrganizationIdErrorComponentAttr:
    if value in API_V1_INCIDENTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_UPDATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
