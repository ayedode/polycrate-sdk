from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contacts_update_address_error_component import ApiV1ContactsUpdateAddressErrorComponent
    from ..models.api_v1_contacts_update_city_error_component import ApiV1ContactsUpdateCityErrorComponent
    from ..models.api_v1_contacts_update_contact_role_error_component import (
        ApiV1ContactsUpdateContactRoleErrorComponent,
    )
    from ..models.api_v1_contacts_update_country_error_component import ApiV1ContactsUpdateCountryErrorComponent
    from ..models.api_v1_contacts_update_credential_id_error_component import (
        ApiV1ContactsUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_contacts_update_email_error_component import ApiV1ContactsUpdateEmailErrorComponent
    from ..models.api_v1_contacts_update_firstname_error_component import ApiV1ContactsUpdateFirstnameErrorComponent
    from ..models.api_v1_contacts_update_is_billing_contact_error_component import (
        ApiV1ContactsUpdateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_contacts_update_is_maintenance_contact_error_component import (
        ApiV1ContactsUpdateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_contacts_update_keycloak_user_id_error_component import (
        ApiV1ContactsUpdateKeycloakUserIdErrorComponent,
    )
    from ..models.api_v1_contacts_update_kind_error_component import ApiV1ContactsUpdateKindErrorComponent
    from ..models.api_v1_contacts_update_last_sync_at_error_component import ApiV1ContactsUpdateLastSyncAtErrorComponent
    from ..models.api_v1_contacts_update_lastname_error_component import ApiV1ContactsUpdateLastnameErrorComponent
    from ..models.api_v1_contacts_update_name_error_component import ApiV1ContactsUpdateNameErrorComponent
    from ..models.api_v1_contacts_update_non_field_errors_error_component import (
        ApiV1ContactsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_contacts_update_note_error_component import ApiV1ContactsUpdateNoteErrorComponent
    from ..models.api_v1_contacts_update_organization_id_error_component import (
        ApiV1ContactsUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_contacts_update_phone_error_component import ApiV1ContactsUpdatePhoneErrorComponent
    from ..models.api_v1_contacts_update_sync_source_error_component import ApiV1ContactsUpdateSyncSourceErrorComponent
    from ..models.api_v1_contacts_update_zipcode_error_component import ApiV1ContactsUpdateZipcodeErrorComponent


T = TypeVar("T", bound="ApiV1ContactsUpdateValidationError")


@_attrs_define
class ApiV1ContactsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactsUpdateAddressErrorComponent | ApiV1ContactsUpdateCityErrorComponent |
            ApiV1ContactsUpdateContactRoleErrorComponent | ApiV1ContactsUpdateCountryErrorComponent |
            ApiV1ContactsUpdateCredentialIdErrorComponent | ApiV1ContactsUpdateEmailErrorComponent |
            ApiV1ContactsUpdateFirstnameErrorComponent | ApiV1ContactsUpdateIsBillingContactErrorComponent |
            ApiV1ContactsUpdateIsMaintenanceContactErrorComponent | ApiV1ContactsUpdateKeycloakUserIdErrorComponent |
            ApiV1ContactsUpdateKindErrorComponent | ApiV1ContactsUpdateLastnameErrorComponent |
            ApiV1ContactsUpdateLastSyncAtErrorComponent | ApiV1ContactsUpdateNameErrorComponent |
            ApiV1ContactsUpdateNonFieldErrorsErrorComponent | ApiV1ContactsUpdateNoteErrorComponent |
            ApiV1ContactsUpdateOrganizationIdErrorComponent | ApiV1ContactsUpdatePhoneErrorComponent |
            ApiV1ContactsUpdateSyncSourceErrorComponent | ApiV1ContactsUpdateZipcodeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactsUpdateAddressErrorComponent
        | ApiV1ContactsUpdateCityErrorComponent
        | ApiV1ContactsUpdateContactRoleErrorComponent
        | ApiV1ContactsUpdateCountryErrorComponent
        | ApiV1ContactsUpdateCredentialIdErrorComponent
        | ApiV1ContactsUpdateEmailErrorComponent
        | ApiV1ContactsUpdateFirstnameErrorComponent
        | ApiV1ContactsUpdateIsBillingContactErrorComponent
        | ApiV1ContactsUpdateIsMaintenanceContactErrorComponent
        | ApiV1ContactsUpdateKeycloakUserIdErrorComponent
        | ApiV1ContactsUpdateKindErrorComponent
        | ApiV1ContactsUpdateLastnameErrorComponent
        | ApiV1ContactsUpdateLastSyncAtErrorComponent
        | ApiV1ContactsUpdateNameErrorComponent
        | ApiV1ContactsUpdateNonFieldErrorsErrorComponent
        | ApiV1ContactsUpdateNoteErrorComponent
        | ApiV1ContactsUpdateOrganizationIdErrorComponent
        | ApiV1ContactsUpdatePhoneErrorComponent
        | ApiV1ContactsUpdateSyncSourceErrorComponent
        | ApiV1ContactsUpdateZipcodeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contacts_update_address_error_component import ApiV1ContactsUpdateAddressErrorComponent
        from ..models.api_v1_contacts_update_city_error_component import ApiV1ContactsUpdateCityErrorComponent
        from ..models.api_v1_contacts_update_contact_role_error_component import (
            ApiV1ContactsUpdateContactRoleErrorComponent,
        )
        from ..models.api_v1_contacts_update_country_error_component import ApiV1ContactsUpdateCountryErrorComponent
        from ..models.api_v1_contacts_update_credential_id_error_component import (
            ApiV1ContactsUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_contacts_update_email_error_component import ApiV1ContactsUpdateEmailErrorComponent
        from ..models.api_v1_contacts_update_firstname_error_component import ApiV1ContactsUpdateFirstnameErrorComponent
        from ..models.api_v1_contacts_update_is_billing_contact_error_component import (
            ApiV1ContactsUpdateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_contacts_update_is_maintenance_contact_error_component import (
            ApiV1ContactsUpdateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_contacts_update_keycloak_user_id_error_component import (
            ApiV1ContactsUpdateKeycloakUserIdErrorComponent,
        )
        from ..models.api_v1_contacts_update_kind_error_component import ApiV1ContactsUpdateKindErrorComponent
        from ..models.api_v1_contacts_update_lastname_error_component import ApiV1ContactsUpdateLastnameErrorComponent
        from ..models.api_v1_contacts_update_name_error_component import ApiV1ContactsUpdateNameErrorComponent
        from ..models.api_v1_contacts_update_non_field_errors_error_component import (
            ApiV1ContactsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_contacts_update_note_error_component import ApiV1ContactsUpdateNoteErrorComponent
        from ..models.api_v1_contacts_update_organization_id_error_component import (
            ApiV1ContactsUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_contacts_update_phone_error_component import ApiV1ContactsUpdatePhoneErrorComponent
        from ..models.api_v1_contacts_update_sync_source_error_component import (
            ApiV1ContactsUpdateSyncSourceErrorComponent,
        )
        from ..models.api_v1_contacts_update_zipcode_error_component import ApiV1ContactsUpdateZipcodeErrorComponent

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateFirstnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateLastnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateZipcodeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateNoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateContactRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateIsBillingContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateKeycloakUserIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsUpdateSyncSourceErrorComponent):
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
        from ..models.api_v1_contacts_update_address_error_component import ApiV1ContactsUpdateAddressErrorComponent
        from ..models.api_v1_contacts_update_city_error_component import ApiV1ContactsUpdateCityErrorComponent
        from ..models.api_v1_contacts_update_contact_role_error_component import (
            ApiV1ContactsUpdateContactRoleErrorComponent,
        )
        from ..models.api_v1_contacts_update_country_error_component import ApiV1ContactsUpdateCountryErrorComponent
        from ..models.api_v1_contacts_update_credential_id_error_component import (
            ApiV1ContactsUpdateCredentialIdErrorComponent,
        )
        from ..models.api_v1_contacts_update_email_error_component import ApiV1ContactsUpdateEmailErrorComponent
        from ..models.api_v1_contacts_update_firstname_error_component import ApiV1ContactsUpdateFirstnameErrorComponent
        from ..models.api_v1_contacts_update_is_billing_contact_error_component import (
            ApiV1ContactsUpdateIsBillingContactErrorComponent,
        )
        from ..models.api_v1_contacts_update_is_maintenance_contact_error_component import (
            ApiV1ContactsUpdateIsMaintenanceContactErrorComponent,
        )
        from ..models.api_v1_contacts_update_keycloak_user_id_error_component import (
            ApiV1ContactsUpdateKeycloakUserIdErrorComponent,
        )
        from ..models.api_v1_contacts_update_kind_error_component import ApiV1ContactsUpdateKindErrorComponent
        from ..models.api_v1_contacts_update_last_sync_at_error_component import (
            ApiV1ContactsUpdateLastSyncAtErrorComponent,
        )
        from ..models.api_v1_contacts_update_lastname_error_component import ApiV1ContactsUpdateLastnameErrorComponent
        from ..models.api_v1_contacts_update_name_error_component import ApiV1ContactsUpdateNameErrorComponent
        from ..models.api_v1_contacts_update_non_field_errors_error_component import (
            ApiV1ContactsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_contacts_update_note_error_component import ApiV1ContactsUpdateNoteErrorComponent
        from ..models.api_v1_contacts_update_organization_id_error_component import (
            ApiV1ContactsUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_contacts_update_phone_error_component import ApiV1ContactsUpdatePhoneErrorComponent
        from ..models.api_v1_contacts_update_sync_source_error_component import (
            ApiV1ContactsUpdateSyncSourceErrorComponent,
        )
        from ..models.api_v1_contacts_update_zipcode_error_component import ApiV1ContactsUpdateZipcodeErrorComponent

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactsUpdateAddressErrorComponent
                | ApiV1ContactsUpdateCityErrorComponent
                | ApiV1ContactsUpdateContactRoleErrorComponent
                | ApiV1ContactsUpdateCountryErrorComponent
                | ApiV1ContactsUpdateCredentialIdErrorComponent
                | ApiV1ContactsUpdateEmailErrorComponent
                | ApiV1ContactsUpdateFirstnameErrorComponent
                | ApiV1ContactsUpdateIsBillingContactErrorComponent
                | ApiV1ContactsUpdateIsMaintenanceContactErrorComponent
                | ApiV1ContactsUpdateKeycloakUserIdErrorComponent
                | ApiV1ContactsUpdateKindErrorComponent
                | ApiV1ContactsUpdateLastnameErrorComponent
                | ApiV1ContactsUpdateLastSyncAtErrorComponent
                | ApiV1ContactsUpdateNameErrorComponent
                | ApiV1ContactsUpdateNonFieldErrorsErrorComponent
                | ApiV1ContactsUpdateNoteErrorComponent
                | ApiV1ContactsUpdateOrganizationIdErrorComponent
                | ApiV1ContactsUpdatePhoneErrorComponent
                | ApiV1ContactsUpdateSyncSourceErrorComponent
                | ApiV1ContactsUpdateZipcodeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_0 = (
                        ApiV1ContactsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_1 = (
                        ApiV1ContactsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_2 = (
                        ApiV1ContactsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_3 = (
                        ApiV1ContactsUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_4 = (
                        ApiV1ContactsUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_5 = (
                        ApiV1ContactsUpdateFirstnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_6 = (
                        ApiV1ContactsUpdateLastnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_7 = (
                        ApiV1ContactsUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_8 = (
                        ApiV1ContactsUpdatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_9 = (
                        ApiV1ContactsUpdateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_10 = (
                        ApiV1ContactsUpdateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_11 = (
                        ApiV1ContactsUpdateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_12 = (
                        ApiV1ContactsUpdateZipcodeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_13 = (
                        ApiV1ContactsUpdateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_14 = (
                        ApiV1ContactsUpdateContactRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_15 = (
                        ApiV1ContactsUpdateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_16 = (
                        ApiV1ContactsUpdateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_17 = (
                        ApiV1ContactsUpdateKeycloakUserIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_update_error_type_18 = (
                        ApiV1ContactsUpdateSyncSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contacts_update_error_type_19 = (
                    ApiV1ContactsUpdateLastSyncAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contacts_update_error_type_19

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contacts_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contacts_update_validation_error.additional_properties = d
        return api_v1_contacts_update_validation_error

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
