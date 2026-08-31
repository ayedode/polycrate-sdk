from typing import Literal

ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_idp_identityproviders_update_annotations_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
