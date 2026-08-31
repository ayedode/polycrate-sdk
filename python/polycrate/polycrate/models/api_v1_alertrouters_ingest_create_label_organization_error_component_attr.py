from typing import Literal

ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponentAttr = Literal["label_organization"]

API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponentAttr
] = {
    "label_organization",
}


def check_api_v1_alertrouters_ingest_create_label_organization_error_component_attr(
    value: str,
) -> ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_INGEST_CREATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
