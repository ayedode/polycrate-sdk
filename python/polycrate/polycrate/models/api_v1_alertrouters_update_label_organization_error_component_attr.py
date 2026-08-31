from typing import Literal

ApiV1AlertroutersUpdateLabelOrganizationErrorComponentAttr = Literal["label_organization"]

API_V1_ALERTROUTERS_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateLabelOrganizationErrorComponentAttr
] = {
    "label_organization",
}


def check_api_v1_alertrouters_update_label_organization_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateLabelOrganizationErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_LABEL_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
