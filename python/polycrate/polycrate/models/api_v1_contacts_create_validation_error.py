from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contacts_create_address_error_component import ApiV1ContactsCreateAddressErrorComponent
    from ..models.api_v1_contacts_create_city_error_component import ApiV1ContactsCreateCityErrorComponent
    from ..models.api_v1_contacts_create_contact_role_error_component import (
        ApiV1ContactsCreateContactRoleErrorComponent,
    )
    from ..models.api_v1_contacts_create_country_error_component import ApiV1ContactsCreateCountryErrorComponent
    from ..models.api_v1_contacts_create_credential_id_error_component import (
        ApiV1ContactsCreateCredentialIdErrorComponent,
    )
    from ..models.api_v1_contacts_create_email_error_component import ApiV1ContactsCreateEmailErrorComponent
    from ..models.api_v1_contacts_create_firstname_error_component import ApiV1ContactsCreateFirstnameErrorComponent
    from ..models.api_v1_contacts_create_is_billing_contact_error_component import (
        ApiV1ContactsCreateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_contacts_create_is_maintenance_contact_error_component import (
        ApiV1ContactsCreateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_contacts_create_keycloak_user_id_error_component import (
        ApiV1ContactsCreateKeycloakUserIdErrorComponent,
    )
    from ..models.api_v1_contacts_create_kind_error_component import ApiV1ContactsCreateKindErrorComponent
    from ..models.api_v1_contacts_create_last_sync_at_error_component import ApiV1ContactsCreateLastSyncAtErrorComponent
    from ..models.api_v1_contacts_create_lastname_error_component import ApiV1ContactsCreateLastnameErrorComponent
    from ..models.api_v1_contacts_create_name_error_component import ApiV1ContactsCreateNameErrorComponent
    from ..models.api_v1_contacts_create_non_field_errors_error_component import (
        ApiV1ContactsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_contacts_create_note_error_component import ApiV1ContactsCreateNoteErrorComponent
    from ..models.api_v1_contacts_create_organization_id_error_component import (
        ApiV1ContactsCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_contacts_create_phone_error_component import ApiV1ContactsCreatePhoneErrorComponent
    from ..models.api_v1_contacts_create_sync_source_error_component import ApiV1ContactsCreateSyncSourceErrorComponent
    from ..models.api_v1_contacts_create_zipcode_error_component import ApiV1ContactsCreateZipcodeErrorComponent


T = TypeVar("T", bound="ApiV1ContactsCreateValidationError")


@_attrs_define
class ApiV1ContactsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactsCreateAddressErrorComponent | ApiV1ContactsCreateCityErrorComponent |
            ApiV1ContactsCreateContactRoleErrorComponent | ApiV1ContactsCreateCountryErrorComponent |
            ApiV1ContactsCreateCredentialIdErrorComponent | ApiV1ContactsCreateEmailErrorComponent |
            ApiV1ContactsCreateFirstnameErrorComponent | ApiV1ContactsCreateIsBillingContactErrorComponent |
            ApiV1ContactsCreateIsMaintenanceContactErrorComponent | ApiV1ContactsCreateKeycloakUserIdErrorComponent |
            ApiV1ContactsCreateKindErrorComponent | ApiV1ContactsCreateLastnameErrorComponent |
            ApiV1ContactsCreateLastSyncAtErrorComponent | ApiV1ContactsCreateNameErrorComponent |
            ApiV1ContactsCreateNonFieldErrorsErrorComponent | ApiV1ContactsCreateNoteErrorComponent |
            ApiV1ContactsCreateOrganizationIdErrorComponent | ApiV1ContactsCreatePhoneErrorComponent |
            ApiV1ContactsCreateSyncSourceErrorComponent | ApiV1ContactsCreateZipcodeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactsCreateAddressErrorComponent
        | ApiV1ContactsCreateCityErrorComponent
        | ApiV1ContactsCreateContactRoleErrorComponent
        | ApiV1ContactsCreateCountryErrorComponent
        | ApiV1ContactsCreateCredentialIdErrorComponent
        | ApiV1ContactsCreateEmailErrorComponent
        | ApiV1ContactsCreateFirstnameErrorComponent
        | ApiV1ContactsCreateIsBillingContactErrorComponent
        | ApiV1ContactsCreateIsMaintenanceContactErrorComponent
        | ApiV1ContactsCreateKeycloakUserIdErrorComponent
        | ApiV1ContactsCreateKindErrorComponent
        | ApiV1ContactsCreateLastnameErrorComponent
        | ApiV1ContactsCreateLastSyncAtErrorComponent
        | ApiV1ContactsCreateNameErrorComponent
        | ApiV1ContactsCreateNonFieldErrorsErrorComponent
        | ApiV1ContactsCreateNoteErrorComponent
        | ApiV1ContactsCreateOrganizationIdErrorComponent
        | ApiV1ContactsCreatePhoneErrorComponent
        | ApiV1ContactsCreateSyncSourceErrorComponent
        | ApiV1ContactsCreateZipcodeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contacts_create_address_error_component import ApiV1ContactsCreateAddressErrorComponent
        from ..models.api_v1_contacts_create_city_error_component import ApiV1ContactsCreateCityErrorComponent
        from ..models.api_v1_contacts_create_contact_role_error_component import (
            ApiV1ContactsCreateContactRoleErrorComponent,
        )
        from ..models.api_v1_contacts_create_country_error_component import ApiV1ContactsCreateCountryErrorComponent
        from ..models.api_v1_contacts_create_credential_id_error_component import (
            ApiV1ContactsCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_contacts_create_email_error_component import ApiV1ContactsCreateEmailErrorComponent
        from ..models.api_v1_contacts_create_firstname_error_component import ApiV1ContactsCreateFirstnameErrorComponent
        from ..models.api_v1_contacts_create_is_billing_contact_error_component import (
            ApiV1ContactsCreateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_contacts_create_is_maintenance_contact_error_component import (
            ApiV1ContactsCreateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_contacts_create_keycloak_user_id_error_component import (
            ApiV1ContactsCreateKeycloakUserIdErrorComponent,
        )
        from ..models.api_v1_contacts_create_kind_error_component import ApiV1ContactsCreateKindErrorComponent
        from ..models.api_v1_contacts_create_lastname_error_component import ApiV1ContactsCreateLastnameErrorComponent
        from ..models.api_v1_contacts_create_name_error_component import ApiV1ContactsCreateNameErrorComponent
        from ..models.api_v1_contacts_create_non_field_errors_error_component import (
            ApiV1ContactsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_contacts_create_note_error_component import ApiV1ContactsCreateNoteErrorComponent
        from ..models.api_v1_contacts_create_organization_id_error_component import (
            ApiV1ContactsCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_contacts_create_phone_error_component import ApiV1ContactsCreatePhoneErrorComponent
        from ..models.api_v1_contacts_create_sync_source_error_component import (
            ApiV1ContactsCreateSyncSourceErrorComponent,
        )
        from ..models.api_v1_contacts_create_zipcode_error_component import ApiV1ContactsCreateZipcodeErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateFirstnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateLastnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateZipcodeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateNoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateContactRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateIsBillingContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateKeycloakUserIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsCreateSyncSourceErrorComponent):
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
        from ..models.api_v1_contacts_create_address_error_component import ApiV1ContactsCreateAddressErrorComponent
        from ..models.api_v1_contacts_create_city_error_component import ApiV1ContactsCreateCityErrorComponent
        from ..models.api_v1_contacts_create_contact_role_error_component import (
            ApiV1ContactsCreateContactRoleErrorComponent,
        )
        from ..models.api_v1_contacts_create_country_error_component import ApiV1ContactsCreateCountryErrorComponent
        from ..models.api_v1_contacts_create_credential_id_error_component import (
            ApiV1ContactsCreateCredentialIdErrorComponent,
        )
        from ..models.api_v1_contacts_create_email_error_component import ApiV1ContactsCreateEmailErrorComponent
        from ..models.api_v1_contacts_create_firstname_error_component import ApiV1ContactsCreateFirstnameErrorComponent
        from ..models.api_v1_contacts_create_is_billing_contact_error_component import (
            ApiV1ContactsCreateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_contacts_create_is_maintenance_contact_error_component import (
            ApiV1ContactsCreateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_contacts_create_keycloak_user_id_error_component import (
            ApiV1ContactsCreateKeycloakUserIdErrorComponent,
        )
        from ..models.api_v1_contacts_create_kind_error_component import ApiV1ContactsCreateKindErrorComponent
        from ..models.api_v1_contacts_create_last_sync_at_error_component import (
            ApiV1ContactsCreateLastSyncAtErrorComponent,
        )
        from ..models.api_v1_contacts_create_lastname_error_component import ApiV1ContactsCreateLastnameErrorComponent
        from ..models.api_v1_contacts_create_name_error_component import ApiV1ContactsCreateNameErrorComponent
        from ..models.api_v1_contacts_create_non_field_errors_error_component import (
            ApiV1ContactsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_contacts_create_note_error_component import ApiV1ContactsCreateNoteErrorComponent
        from ..models.api_v1_contacts_create_organization_id_error_component import (
            ApiV1ContactsCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_contacts_create_phone_error_component import ApiV1ContactsCreatePhoneErrorComponent
        from ..models.api_v1_contacts_create_sync_source_error_component import (
            ApiV1ContactsCreateSyncSourceErrorComponent,
        )
        from ..models.api_v1_contacts_create_zipcode_error_component import ApiV1ContactsCreateZipcodeErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactsCreateAddressErrorComponent
                | ApiV1ContactsCreateCityErrorComponent
                | ApiV1ContactsCreateContactRoleErrorComponent
                | ApiV1ContactsCreateCountryErrorComponent
                | ApiV1ContactsCreateCredentialIdErrorComponent
                | ApiV1ContactsCreateEmailErrorComponent
                | ApiV1ContactsCreateFirstnameErrorComponent
                | ApiV1ContactsCreateIsBillingContactErrorComponent
                | ApiV1ContactsCreateIsMaintenanceContactErrorComponent
                | ApiV1ContactsCreateKeycloakUserIdErrorComponent
                | ApiV1ContactsCreateKindErrorComponent
                | ApiV1ContactsCreateLastnameErrorComponent
                | ApiV1ContactsCreateLastSyncAtErrorComponent
                | ApiV1ContactsCreateNameErrorComponent
                | ApiV1ContactsCreateNonFieldErrorsErrorComponent
                | ApiV1ContactsCreateNoteErrorComponent
                | ApiV1ContactsCreateOrganizationIdErrorComponent
                | ApiV1ContactsCreatePhoneErrorComponent
                | ApiV1ContactsCreateSyncSourceErrorComponent
                | ApiV1ContactsCreateZipcodeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_0 = (
                        ApiV1ContactsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_1 = (
                        ApiV1ContactsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_2 = (
                        ApiV1ContactsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_3 = (
                        ApiV1ContactsCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_4 = (
                        ApiV1ContactsCreateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_5 = (
                        ApiV1ContactsCreateFirstnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_6 = (
                        ApiV1ContactsCreateLastnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_7 = (
                        ApiV1ContactsCreateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_8 = (
                        ApiV1ContactsCreatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_9 = (
                        ApiV1ContactsCreateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_10 = (
                        ApiV1ContactsCreateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_11 = (
                        ApiV1ContactsCreateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_12 = (
                        ApiV1ContactsCreateZipcodeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_13 = (
                        ApiV1ContactsCreateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_14 = (
                        ApiV1ContactsCreateContactRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_15 = (
                        ApiV1ContactsCreateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_16 = (
                        ApiV1ContactsCreateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_17 = (
                        ApiV1ContactsCreateKeycloakUserIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_create_error_type_18 = (
                        ApiV1ContactsCreateSyncSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contacts_create_error_type_19 = (
                    ApiV1ContactsCreateLastSyncAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contacts_create_error_type_19

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contacts_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contacts_create_validation_error.additional_properties = d
        return api_v1_contacts_create_validation_error

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
