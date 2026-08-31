from typing import Literal

ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_domains_dnszones_rectify_create_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
