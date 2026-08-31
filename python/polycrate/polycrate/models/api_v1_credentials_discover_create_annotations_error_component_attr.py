from typing import Literal

ApiV1CredentialsDiscoverCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_CREDENTIALS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsDiscoverCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_credentials_discover_create_annotations_error_component_attr(
    value: str,
) -> ApiV1CredentialsDiscoverCreateAnnotationsErrorComponentAttr:
    if value in API_V1_CREDENTIALS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_DISCOVER_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
