from typing import Literal

ApiV1DomainsDnszonesCreateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_DOMAINS_DNSZONES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_domains_dnszones_create_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
