from typing import Literal

ApiV1OrganizationsUpdateOwnerIdErrorComponentAttr = Literal["owner_id"]

API_V1_ORGANIZATIONS_UPDATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateOwnerIdErrorComponentAttr
] = {
    "owner_id",
}


def check_api_v1_organizations_update_owner_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateOwnerIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_OWNER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
