from typing import Literal

ApiV1OrganizationsUpdateLegalNameErrorComponentAttr = Literal["legal_name"]

API_V1_ORGANIZATIONS_UPDATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateLegalNameErrorComponentAttr
] = {
    "legal_name",
}


def check_api_v1_organizations_update_legal_name_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateLegalNameErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
