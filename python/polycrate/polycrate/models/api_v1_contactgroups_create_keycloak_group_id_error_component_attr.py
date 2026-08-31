from typing import Literal

ApiV1ContactgroupsCreateKeycloakGroupIdErrorComponentAttr = Literal["keycloak_group_id"]

API_V1_CONTACTGROUPS_CREATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsCreateKeycloakGroupIdErrorComponentAttr
] = {
    "keycloak_group_id",
}


def check_api_v1_contactgroups_create_keycloak_group_id_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsCreateKeycloakGroupIdErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_CREATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_CREATE_KEYCLOAK_GROUP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
