from typing import Literal

ApiV1DomainsDomainsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAINS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domains_create_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
