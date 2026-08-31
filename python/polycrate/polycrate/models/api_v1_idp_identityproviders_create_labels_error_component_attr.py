from typing import Literal

ApiV1IdpIdentityprovidersCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_idp_identityproviders_create_labels_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateLabelsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
