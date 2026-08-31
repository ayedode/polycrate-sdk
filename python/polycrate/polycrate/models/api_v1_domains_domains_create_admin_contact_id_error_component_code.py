from typing import Literal

ApiV1DomainsDomainsCreateAdminContactIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAINS_CREATE_ADMIN_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateAdminContactIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domains_create_admin_contact_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateAdminContactIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ADMIN_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ADMIN_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
