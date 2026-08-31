from typing import Literal

ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_domains_dnszones_partial_update_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
