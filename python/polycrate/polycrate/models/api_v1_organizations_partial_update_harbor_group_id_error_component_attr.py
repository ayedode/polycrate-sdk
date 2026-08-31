from typing import Literal

ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponentAttr = Literal["harbor_group_id"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponentAttr
] = {
    "harbor_group_id",
}


def check_api_v1_organizations_partial_update_harbor_group_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateHarborGroupIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_HARBOR_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
