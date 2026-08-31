from typing import Literal

ApiV1DomainsDnszonesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_DOMAINS_DNSZONES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_domains_dnszones_create_labels_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesCreateLabelsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
