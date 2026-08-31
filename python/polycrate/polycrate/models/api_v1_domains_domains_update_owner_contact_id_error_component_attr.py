from typing import Literal

ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponentAttr = Literal["owner_contact_id"]

API_V1_DOMAINS_DOMAINS_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponentAttr
] = {
    "owner_contact_id",
}


def check_api_v1_domains_domains_update_owner_contact_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateOwnerContactIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
