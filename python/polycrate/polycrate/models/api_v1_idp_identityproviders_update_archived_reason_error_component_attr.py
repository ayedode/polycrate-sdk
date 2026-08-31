from typing import Literal

ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_idp_identityproviders_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
