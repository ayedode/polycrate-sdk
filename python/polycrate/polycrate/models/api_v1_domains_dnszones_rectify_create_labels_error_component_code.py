from typing import Literal

ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_rectify_create_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
