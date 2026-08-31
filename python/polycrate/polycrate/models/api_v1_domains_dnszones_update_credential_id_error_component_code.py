from typing import Literal

ApiV1DomainsDnszonesUpdateCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DNSZONES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdateCredentialIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_dnszones_update_credential_id_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdateCredentialIdErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
