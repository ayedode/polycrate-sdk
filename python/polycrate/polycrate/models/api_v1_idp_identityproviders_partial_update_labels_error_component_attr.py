from typing import Literal

ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_idp_identityproviders_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
