from typing import Literal

ApiV1DomainsDnszonesUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DNSZONES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_dnszones_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
