from typing import Literal

ApiV1ContactsCreateKeycloakUserIdErrorComponentAttr = Literal["keycloak_user_id"]

API_V1_CONTACTS_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactsCreateKeycloakUserIdErrorComponentAttr
] = {
    "keycloak_user_id",
}


def check_api_v1_contacts_create_keycloak_user_id_error_component_attr(
    value: str,
) -> ApiV1ContactsCreateKeycloakUserIdErrorComponentAttr:
    if value in API_V1_CONTACTS_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_CREATE_KEYCLOAK_USER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
