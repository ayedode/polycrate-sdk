from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type"
]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_managed_by_content_type_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateManagedByContentTypeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_MANAGED_BY_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
