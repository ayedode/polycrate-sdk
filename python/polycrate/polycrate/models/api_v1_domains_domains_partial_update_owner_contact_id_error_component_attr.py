from typing import Literal

ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponentAttr = Literal["owner_contact_id"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponentAttr
] = {
    "owner_contact_id",
}


def check_api_v1_domains_domains_partial_update_owner_contact_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
