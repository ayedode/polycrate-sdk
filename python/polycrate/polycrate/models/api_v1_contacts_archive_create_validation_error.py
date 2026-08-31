from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contacts_archive_create_address_error_component import (
        ApiV1ContactsArchiveCreateAddressErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_city_error_component import (
        ApiV1ContactsArchiveCreateCityErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_contact_role_error_component import (
        ApiV1ContactsArchiveCreateContactRoleErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_country_error_component import (
        ApiV1ContactsArchiveCreateCountryErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_credential_id_error_component import (
        ApiV1ContactsArchiveCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_email_error_component import (
        ApiV1ContactsArchiveCreateEmailErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_firstname_error_component import (
        ApiV1ContactsArchiveCreateFirstnameErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_is_billing_contact_error_component import (
        ApiV1ContactsArchiveCreateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_is_maintenance_contact_error_component import (
        ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_keycloak_user_id_error_component import (
        ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_kind_error_component import (
        ApiV1ContactsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_last_sync_at_error_component import (
        ApiV1ContactsArchiveCreateLastSyncAtErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_lastname_error_component import (
        ApiV1ContactsArchiveCreateLastnameErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_name_error_component import (
        ApiV1ContactsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_non_field_errors_error_component import (
        ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_note_error_component import (
        ApiV1ContactsArchiveCreateNoteErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_organization_id_error_component import (
        ApiV1ContactsArchiveCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_phone_error_component import (
        ApiV1ContactsArchiveCreatePhoneErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_sync_source_error_component import (
        ApiV1ContactsArchiveCreateSyncSourceErrorComponent,
    )
    from ..models.api_v1_contacts_archive_create_zipcode_error_component import (
        ApiV1ContactsArchiveCreateZipcodeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ContactsArchiveCreateValidationError")


@_attrs_define
class ApiV1ContactsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactsArchiveCreateAddressErrorComponent | ApiV1ContactsArchiveCreateCityErrorComponent |
            ApiV1ContactsArchiveCreateContactRoleErrorComponent | ApiV1ContactsArchiveCreateCountryErrorComponent |
            ApiV1ContactsArchiveCreateCredentialIdErrorComponent | ApiV1ContactsArchiveCreateEmailErrorComponent |
            ApiV1ContactsArchiveCreateFirstnameErrorComponent | ApiV1ContactsArchiveCreateIsBillingContactErrorComponent |
            ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent |
            ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent | ApiV1ContactsArchiveCreateKindErrorComponent |
            ApiV1ContactsArchiveCreateLastnameErrorComponent | ApiV1ContactsArchiveCreateLastSyncAtErrorComponent |
            ApiV1ContactsArchiveCreateNameErrorComponent | ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1ContactsArchiveCreateNoteErrorComponent | ApiV1ContactsArchiveCreateOrganizationIdErrorComponent |
            ApiV1ContactsArchiveCreatePhoneErrorComponent | ApiV1ContactsArchiveCreateSyncSourceErrorComponent |
            ApiV1ContactsArchiveCreateZipcodeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactsArchiveCreateAddressErrorComponent
        | ApiV1ContactsArchiveCreateCityErrorComponent
        | ApiV1ContactsArchiveCreateContactRoleErrorComponent
        | ApiV1ContactsArchiveCreateCountryErrorComponent
        | ApiV1ContactsArchiveCreateCredentialIdErrorComponent
        | ApiV1ContactsArchiveCreateEmailErrorComponent
        | ApiV1ContactsArchiveCreateFirstnameErrorComponent
        | ApiV1ContactsArchiveCreateIsBillingContactErrorComponent
        | ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent
        | ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent
        | ApiV1ContactsArchiveCreateKindErrorComponent
        | ApiV1ContactsArchiveCreateLastnameErrorComponent
        | ApiV1ContactsArchiveCreateLastSyncAtErrorComponent
        | ApiV1ContactsArchiveCreateNameErrorComponent
        | ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1ContactsArchiveCreateNoteErrorComponent
        | ApiV1ContactsArchiveCreateOrganizationIdErrorComponent
        | ApiV1ContactsArchiveCreatePhoneErrorComponent
        | ApiV1ContactsArchiveCreateSyncSourceErrorComponent
        | ApiV1ContactsArchiveCreateZipcodeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contacts_archive_create_address_error_component import (
            ApiV1ContactsArchiveCreateAddressErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_city_error_component import (
            ApiV1ContactsArchiveCreateCityErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_contact_role_error_component import (
            ApiV1ContactsArchiveCreateContactRoleErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_country_error_component import (
            ApiV1ContactsArchiveCreateCountryErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_credential_id_error_component import (
            ApiV1ContactsArchiveCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_email_error_component import (
            ApiV1ContactsArchiveCreateEmailErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_firstname_error_component import (
            ApiV1ContactsArchiveCreateFirstnameErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_is_billing_contact_error_component import (
            ApiV1ContactsArchiveCreateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_is_maintenance_contact_error_component import (
            ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_keycloak_user_id_error_component import (
            ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_kind_error_component import (
            ApiV1ContactsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_lastname_error_component import (
            ApiV1ContactsArchiveCreateLastnameErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_name_error_component import (
            ApiV1ContactsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_non_field_errors_error_component import (
            ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_note_error_component import (
            ApiV1ContactsArchiveCreateNoteErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_organization_id_error_component import (
            ApiV1ContactsArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_phone_error_component import (
            ApiV1ContactsArchiveCreatePhoneErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_sync_source_error_component import (
            ApiV1ContactsArchiveCreateSyncSourceErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_zipcode_error_component import (
            ApiV1ContactsArchiveCreateZipcodeErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateFirstnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateLastnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateZipcodeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateNoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateContactRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateIsBillingContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsArchiveCreateSyncSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_contacts_archive_create_address_error_component import (
            ApiV1ContactsArchiveCreateAddressErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_city_error_component import (
            ApiV1ContactsArchiveCreateCityErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_contact_role_error_component import (
            ApiV1ContactsArchiveCreateContactRoleErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_country_error_component import (
            ApiV1ContactsArchiveCreateCountryErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_credential_id_error_component import (
            ApiV1ContactsArchiveCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_email_error_component import (
            ApiV1ContactsArchiveCreateEmailErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_firstname_error_component import (
            ApiV1ContactsArchiveCreateFirstnameErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_is_billing_contact_error_component import (
            ApiV1ContactsArchiveCreateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_is_maintenance_contact_error_component import (
            ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_keycloak_user_id_error_component import (
            ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_kind_error_component import (
            ApiV1ContactsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_last_sync_at_error_component import (
            ApiV1ContactsArchiveCreateLastSyncAtErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_lastname_error_component import (
            ApiV1ContactsArchiveCreateLastnameErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_name_error_component import (
            ApiV1ContactsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_non_field_errors_error_component import (
            ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_note_error_component import (
            ApiV1ContactsArchiveCreateNoteErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_organization_id_error_component import (
            ApiV1ContactsArchiveCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_phone_error_component import (
            ApiV1ContactsArchiveCreatePhoneErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_sync_source_error_component import (
            ApiV1ContactsArchiveCreateSyncSourceErrorComponent,
        )
        from ..models.api_v1_contacts_archive_create_zipcode_error_component import (
            ApiV1ContactsArchiveCreateZipcodeErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactsArchiveCreateAddressErrorComponent
                | ApiV1ContactsArchiveCreateCityErrorComponent
                | ApiV1ContactsArchiveCreateContactRoleErrorComponent
                | ApiV1ContactsArchiveCreateCountryErrorComponent
                | ApiV1ContactsArchiveCreateCredentialIdErrorComponent
                | ApiV1ContactsArchiveCreateEmailErrorComponent
                | ApiV1ContactsArchiveCreateFirstnameErrorComponent
                | ApiV1ContactsArchiveCreateIsBillingContactErrorComponent
                | ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent
                | ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent
                | ApiV1ContactsArchiveCreateKindErrorComponent
                | ApiV1ContactsArchiveCreateLastnameErrorComponent
                | ApiV1ContactsArchiveCreateLastSyncAtErrorComponent
                | ApiV1ContactsArchiveCreateNameErrorComponent
                | ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1ContactsArchiveCreateNoteErrorComponent
                | ApiV1ContactsArchiveCreateOrganizationIdErrorComponent
                | ApiV1ContactsArchiveCreatePhoneErrorComponent
                | ApiV1ContactsArchiveCreateSyncSourceErrorComponent
                | ApiV1ContactsArchiveCreateZipcodeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_0 = (
                        ApiV1ContactsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_1 = (
                        ApiV1ContactsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_2 = (
                        ApiV1ContactsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_3 = (
                        ApiV1ContactsArchiveCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_4 = (
                        ApiV1ContactsArchiveCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_5 = (
                        ApiV1ContactsArchiveCreateFirstnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_6 = (
                        ApiV1ContactsArchiveCreateLastnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_7 = (
                        ApiV1ContactsArchiveCreateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_8 = (
                        ApiV1ContactsArchiveCreatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_9 = (
                        ApiV1ContactsArchiveCreateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_10 = (
                        ApiV1ContactsArchiveCreateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_11 = (
                        ApiV1ContactsArchiveCreateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_12 = (
                        ApiV1ContactsArchiveCreateZipcodeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_13 = (
                        ApiV1ContactsArchiveCreateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_14 = (
                        ApiV1ContactsArchiveCreateContactRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_15 = (
                        ApiV1ContactsArchiveCreateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_16 = (
                        ApiV1ContactsArchiveCreateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_17 = (
                        ApiV1ContactsArchiveCreateKeycloakUserIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_archive_create_error_type_18 = (
                        ApiV1ContactsArchiveCreateSyncSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contacts_archive_create_error_type_19 = (
                    ApiV1ContactsArchiveCreateLastSyncAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contacts_archive_create_error_type_19

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contacts_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contacts_archive_create_validation_error.additional_properties = d
        return api_v1_contacts_archive_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
