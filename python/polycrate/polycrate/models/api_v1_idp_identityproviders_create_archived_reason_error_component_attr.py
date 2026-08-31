from typing import Literal

ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_IDP_IDENTITYPROVIDERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_idp_identityproviders_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
