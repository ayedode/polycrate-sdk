from typing import Literal

ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_idp_identityproviders_archive_create_annotations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersArchiveCreateAnnotationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_ARCHIVE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
