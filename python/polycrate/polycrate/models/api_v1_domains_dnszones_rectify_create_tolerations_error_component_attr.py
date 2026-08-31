from typing import Literal

ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_dnszones_rectify_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
