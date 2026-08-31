from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_update_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
