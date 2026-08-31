from typing import Literal

ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponentAttr = Literal["label_organization"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponentAttr
] = {
    "label_organization",
}


def check_api_v1_alertrouters_archive_create_label_organization_error_component_attr(
    value: str,
) -> ApiV1AlertroutersArchiveCreateLabelOrganizationErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
