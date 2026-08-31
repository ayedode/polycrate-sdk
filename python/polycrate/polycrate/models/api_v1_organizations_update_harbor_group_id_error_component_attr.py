from typing import Literal

ApiV1OrganizationsUpdateHarborGroupIdErrorComponentAttr = Literal["harbor_group_id"]

API_V1_ORGANIZATIONS_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateHarborGroupIdErrorComponentAttr
] = {
    "harbor_group_id",
}


def check_api_v1_organizations_update_harbor_group_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateHarborGroupIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
