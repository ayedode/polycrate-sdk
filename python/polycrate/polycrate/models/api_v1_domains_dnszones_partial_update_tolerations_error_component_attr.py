from typing import Literal

ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_dnszones_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
