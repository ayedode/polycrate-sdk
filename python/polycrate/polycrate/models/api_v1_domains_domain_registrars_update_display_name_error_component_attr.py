from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_domains_domain_registrars_update_display_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
