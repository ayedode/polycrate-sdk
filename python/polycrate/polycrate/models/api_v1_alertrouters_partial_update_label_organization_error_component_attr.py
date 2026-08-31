from typing import Literal

ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponentAttr = Literal["label_organization"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponentAttr
] = {
    "label_organization",
}


def check_api_v1_alertrouters_partial_update_label_organization_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateLabelOrganizationErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
