from typing import Literal

ApiV1DomainsDomainsCreateAdminContactIdErrorComponentAttr = Literal["admin_contact_id"]

API_V1_DOMAINS_DOMAINS_CREATE_ADMIN_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateAdminContactIdErrorComponentAttr
] = {
    "admin_contact_id",
}


def check_api_v1_domains_domains_create_admin_contact_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateAdminContactIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ADMIN_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ADMIN_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
