from typing import Literal

ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_idp_identityproviders_create_annotations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateAnnotationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
