from typing import Literal

ApiV1AlertroutersIngestCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_ALERTROUTERS_INGEST_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_alertrouters_ingest_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
