from typing import Literal

ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domains_partial_update_owner_contact_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateOwnerContactIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_OWNER_CONTACT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
