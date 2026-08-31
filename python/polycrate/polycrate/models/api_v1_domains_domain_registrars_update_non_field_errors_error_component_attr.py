from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_domains_domain_registrars_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
