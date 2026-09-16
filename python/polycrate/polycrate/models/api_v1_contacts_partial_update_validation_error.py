from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_contacts_partial_update_address_error_component import (
        ApiV1ContactsPartialUpdateAddressErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_city_error_component import (
        ApiV1ContactsPartialUpdateCityErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_contact_role_error_component import (
        ApiV1ContactsPartialUpdateContactRoleErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_country_error_component import (
        ApiV1ContactsPartialUpdateCountryErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_credential_id_error_component import (
        ApiV1ContactsPartialUpdateCredentialIdErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_email_error_component import (
        ApiV1ContactsPartialUpdateEmailErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_firstname_error_component import (
        ApiV1ContactsPartialUpdateFirstnameErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_is_billing_contact_error_component import (
        ApiV1ContactsPartialUpdateIsBillingContactErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_is_maintenance_contact_error_component import (
        ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_keycloak_user_id_error_component import (
        ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_kind_error_component import (
        ApiV1ContactsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_last_sync_at_error_component import (
        ApiV1ContactsPartialUpdateLastSyncAtErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_lastname_error_component import (
        ApiV1ContactsPartialUpdateLastnameErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_name_error_component import (
        ApiV1ContactsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_non_field_errors_error_component import (
        ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_note_error_component import (
        ApiV1ContactsPartialUpdateNoteErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_organization_id_error_component import (
        ApiV1ContactsPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_phone_error_component import (
        ApiV1ContactsPartialUpdatePhoneErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_sync_source_error_component import (
        ApiV1ContactsPartialUpdateSyncSourceErrorComponent,
    )
    from ..models.api_v1_contacts_partial_update_zipcode_error_component import (
        ApiV1ContactsPartialUpdateZipcodeErrorComponent,
    )


T = TypeVar("T", bound="ApiV1ContactsPartialUpdateValidationError")


@_attrs_define
class ApiV1ContactsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1ContactsPartialUpdateAddressErrorComponent | ApiV1ContactsPartialUpdateCityErrorComponent |
            ApiV1ContactsPartialUpdateContactRoleErrorComponent | ApiV1ContactsPartialUpdateCountryErrorComponent |
            ApiV1ContactsPartialUpdateCredentialIdErrorComponent | ApiV1ContactsPartialUpdateEmailErrorComponent |
            ApiV1ContactsPartialUpdateFirstnameErrorComponent | ApiV1ContactsPartialUpdateIsBillingContactErrorComponent |
            ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent |
            ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent | ApiV1ContactsPartialUpdateKindErrorComponent |
            ApiV1ContactsPartialUpdateLastnameErrorComponent | ApiV1ContactsPartialUpdateLastSyncAtErrorComponent |
            ApiV1ContactsPartialUpdateNameErrorComponent | ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1ContactsPartialUpdateNoteErrorComponent | ApiV1ContactsPartialUpdateOrganizationIdErrorComponent |
            ApiV1ContactsPartialUpdatePhoneErrorComponent | ApiV1ContactsPartialUpdateSyncSourceErrorComponent |
            ApiV1ContactsPartialUpdateZipcodeErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1ContactsPartialUpdateAddressErrorComponent
        | ApiV1ContactsPartialUpdateCityErrorComponent
        | ApiV1ContactsPartialUpdateContactRoleErrorComponent
        | ApiV1ContactsPartialUpdateCountryErrorComponent
        | ApiV1ContactsPartialUpdateCredentialIdErrorComponent
        | ApiV1ContactsPartialUpdateEmailErrorComponent
        | ApiV1ContactsPartialUpdateFirstnameErrorComponent
        | ApiV1ContactsPartialUpdateIsBillingContactErrorComponent
        | ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent
        | ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent
        | ApiV1ContactsPartialUpdateKindErrorComponent
        | ApiV1ContactsPartialUpdateLastnameErrorComponent
        | ApiV1ContactsPartialUpdateLastSyncAtErrorComponent
        | ApiV1ContactsPartialUpdateNameErrorComponent
        | ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1ContactsPartialUpdateNoteErrorComponent
        | ApiV1ContactsPartialUpdateOrganizationIdErrorComponent
        | ApiV1ContactsPartialUpdatePhoneErrorComponent
        | ApiV1ContactsPartialUpdateSyncSourceErrorComponent
        | ApiV1ContactsPartialUpdateZipcodeErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_contacts_partial_update_address_error_component import (
            ApiV1ContactsPartialUpdateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_city_error_component import (
            ApiV1ContactsPartialUpdateCityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_contact_role_error_component import (
            ApiV1ContactsPartialUpdateContactRoleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_country_error_component import (
            ApiV1ContactsPartialUpdateCountryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_credential_id_error_component import (
            ApiV1ContactsPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_email_error_component import (
            ApiV1ContactsPartialUpdateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_firstname_error_component import (
            ApiV1ContactsPartialUpdateFirstnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_is_billing_contact_error_component import (
            ApiV1ContactsPartialUpdateIsBillingContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_is_maintenance_contact_error_component import (
            ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_keycloak_user_id_error_component import (
            ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_kind_error_component import (
            ApiV1ContactsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_lastname_error_component import (
            ApiV1ContactsPartialUpdateLastnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_name_error_component import (
            ApiV1ContactsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_non_field_errors_error_component import (
            ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_note_error_component import (
            ApiV1ContactsPartialUpdateNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_organization_id_error_component import (
            ApiV1ContactsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_phone_error_component import (
            ApiV1ContactsPartialUpdatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_sync_source_error_component import (
            ApiV1ContactsPartialUpdateSyncSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_zipcode_error_component import (
            ApiV1ContactsPartialUpdateZipcodeErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateCredentialIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateFirstnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateLastnameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateEmailErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdatePhoneErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateAddressErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateCityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateCountryErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateZipcodeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateNoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateContactRoleErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateIsBillingContactErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1ContactsPartialUpdateSyncSourceErrorComponent):
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
        from ..models.api_v1_contacts_partial_update_address_error_component import (
            ApiV1ContactsPartialUpdateAddressErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_city_error_component import (
            ApiV1ContactsPartialUpdateCityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_contact_role_error_component import (
            ApiV1ContactsPartialUpdateContactRoleErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_country_error_component import (
            ApiV1ContactsPartialUpdateCountryErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_credential_id_error_component import (
            ApiV1ContactsPartialUpdateCredentialIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_email_error_component import (
            ApiV1ContactsPartialUpdateEmailErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_firstname_error_component import (
            ApiV1ContactsPartialUpdateFirstnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_is_billing_contact_error_component import (
            ApiV1ContactsPartialUpdateIsBillingContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_is_maintenance_contact_error_component import (
            ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_keycloak_user_id_error_component import (
            ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_kind_error_component import (
            ApiV1ContactsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_last_sync_at_error_component import (
            ApiV1ContactsPartialUpdateLastSyncAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_lastname_error_component import (
            ApiV1ContactsPartialUpdateLastnameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_name_error_component import (
            ApiV1ContactsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_non_field_errors_error_component import (
            ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_note_error_component import (
            ApiV1ContactsPartialUpdateNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_organization_id_error_component import (
            ApiV1ContactsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_phone_error_component import (
            ApiV1ContactsPartialUpdatePhoneErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_sync_source_error_component import (
            ApiV1ContactsPartialUpdateSyncSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_contacts_partial_update_zipcode_error_component import (
            ApiV1ContactsPartialUpdateZipcodeErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1ContactsPartialUpdateAddressErrorComponent
                | ApiV1ContactsPartialUpdateCityErrorComponent
                | ApiV1ContactsPartialUpdateContactRoleErrorComponent
                | ApiV1ContactsPartialUpdateCountryErrorComponent
                | ApiV1ContactsPartialUpdateCredentialIdErrorComponent
                | ApiV1ContactsPartialUpdateEmailErrorComponent
                | ApiV1ContactsPartialUpdateFirstnameErrorComponent
                | ApiV1ContactsPartialUpdateIsBillingContactErrorComponent
                | ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent
                | ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent
                | ApiV1ContactsPartialUpdateKindErrorComponent
                | ApiV1ContactsPartialUpdateLastnameErrorComponent
                | ApiV1ContactsPartialUpdateLastSyncAtErrorComponent
                | ApiV1ContactsPartialUpdateNameErrorComponent
                | ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1ContactsPartialUpdateNoteErrorComponent
                | ApiV1ContactsPartialUpdateOrganizationIdErrorComponent
                | ApiV1ContactsPartialUpdatePhoneErrorComponent
                | ApiV1ContactsPartialUpdateSyncSourceErrorComponent
                | ApiV1ContactsPartialUpdateZipcodeErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_0 = (
                        ApiV1ContactsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_1 = (
                        ApiV1ContactsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_2 = (
                        ApiV1ContactsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_3 = (
                        ApiV1ContactsPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_4 = (
                        ApiV1ContactsPartialUpdateCredentialIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_5 = (
                        ApiV1ContactsPartialUpdateFirstnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_6 = (
                        ApiV1ContactsPartialUpdateLastnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_7 = (
                        ApiV1ContactsPartialUpdateEmailErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_8 = (
                        ApiV1ContactsPartialUpdatePhoneErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_9 = (
                        ApiV1ContactsPartialUpdateAddressErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_10 = (
                        ApiV1ContactsPartialUpdateCityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_11 = (
                        ApiV1ContactsPartialUpdateCountryErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_12 = (
                        ApiV1ContactsPartialUpdateZipcodeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_13 = (
                        ApiV1ContactsPartialUpdateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_14 = (
                        ApiV1ContactsPartialUpdateContactRoleErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_15 = (
                        ApiV1ContactsPartialUpdateIsMaintenanceContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_16 = (
                        ApiV1ContactsPartialUpdateIsBillingContactErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_17 = (
                        ApiV1ContactsPartialUpdateKeycloakUserIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_contacts_partial_update_error_type_18 = (
                        ApiV1ContactsPartialUpdateSyncSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_contacts_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_contacts_partial_update_error_type_19 = (
                    ApiV1ContactsPartialUpdateLastSyncAtErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_contacts_partial_update_error_type_19

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_contacts_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_contacts_partial_update_validation_error.additional_properties = d
        return api_v1_contacts_partial_update_validation_error

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
