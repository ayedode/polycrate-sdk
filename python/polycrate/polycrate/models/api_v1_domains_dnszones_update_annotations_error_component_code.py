from typing import Literal

ApiV1DomainsDnszonesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_update_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
