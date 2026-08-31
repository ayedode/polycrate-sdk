from typing import Literal

ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponentAttr = Literal["auth_code_credential_id"]

API_V1_DOMAINS_DOMAINS_UPDATE_AUTH_CODE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponentAttr
] = {
    "auth_code_credential_id",
}


def check_api_v1_domains_domains_update_auth_code_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsUpdateAuthCodeCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_UPDATE_AUTH_CODE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_UPDATE_AUTH_CODE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
