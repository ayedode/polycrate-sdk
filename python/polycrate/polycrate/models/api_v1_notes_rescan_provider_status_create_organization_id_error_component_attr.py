from typing import Literal

ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_notes_rescan_provider_status_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
