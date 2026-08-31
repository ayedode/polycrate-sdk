from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_idp_identityproviders_update_annotations_error_component import (
        ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_archived_at_error_component import (
        ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_archived_error_component import (
        ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_archived_reason_error_component import (
        ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_criticality_error_component import (
        ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_debug_mode_error_component import (
        ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_display_name_error_component import (
        ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_hostname_error_component import (
        ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_kind_error_component import (
        ApiV1IdpIdentityprovidersUpdateKindErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_labels_error_component import (
        ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_name_error_component import (
        ApiV1IdpIdentityprovidersUpdateNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_non_field_errors_error_component import (
        ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_platform_service_error_component import (
        ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_provider_error_component import (
        ApiV1IdpIdentityprovidersUpdateProviderErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_provider_id_error_component import (
        ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_provider_reference_error_component import (
        ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_reconciliation_enabled_error_component import (
        ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_sla_availability_error_component import (
        ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_sla_target_error_component import (
        ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_slo_availability_error_component import (
        ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_slo_target_error_component import (
        ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_sync_mode_error_component import (
        ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_target_availability_error_component import (
        ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_update_tolerations_error_component import (
        ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IdpIdentityprovidersUpdateValidationError")


@_attrs_define
class ApiV1IdpIdentityprovidersUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent |
            ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent | ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent
            | ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent |
            ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent |
            ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent |
            ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent | ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent
            | ApiV1IdpIdentityprovidersUpdateKindErrorComponent | ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent |
            ApiV1IdpIdentityprovidersUpdateNameErrorComponent | ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent
            | ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent |
            ApiV1IdpIdentityprovidersUpdateProviderErrorComponent | ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent
            | ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent |
            ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent |
            ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent |
            ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent | ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponent |
            ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent
        | ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent
        | ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent
        | ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent
        | ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent
        | ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent
        | ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent
        | ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent
        | ApiV1IdpIdentityprovidersUpdateKindErrorComponent
        | ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent
        | ApiV1IdpIdentityprovidersUpdateNameErrorComponent
        | ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent
        | ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent
        | ApiV1IdpIdentityprovidersUpdateProviderErrorComponent
        | ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent
        | ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent
        | ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent
        | ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent
        | ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent
        | ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponent
        | ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_idp_identityproviders_update_annotations_error_component import (
            ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_archived_at_error_component import (
            ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_archived_error_component import (
            ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_criticality_error_component import (
            ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_display_name_error_component import (
            ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_hostname_error_component import (
            ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_kind_error_component import (
            ApiV1IdpIdentityprovidersUpdateKindErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_labels_error_component import (
            ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_name_error_component import (
            ApiV1IdpIdentityprovidersUpdateNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_platform_service_error_component import (
            ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_provider_error_component import (
            ApiV1IdpIdentityprovidersUpdateProviderErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_provider_id_error_component import (
            ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_sla_target_error_component import (
            ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_slo_target_error_component import (
            ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_target_availability_error_component import (
            ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_tolerations_error_component import (
            ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent):
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
        from ..models.api_v1_idp_identityproviders_update_annotations_error_component import (
            ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_archived_at_error_component import (
            ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_archived_error_component import (
            ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_criticality_error_component import (
            ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_display_name_error_component import (
            ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_hostname_error_component import (
            ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_kind_error_component import (
            ApiV1IdpIdentityprovidersUpdateKindErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_labels_error_component import (
            ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_name_error_component import (
            ApiV1IdpIdentityprovidersUpdateNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_platform_service_error_component import (
            ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_provider_error_component import (
            ApiV1IdpIdentityprovidersUpdateProviderErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_provider_id_error_component import (
            ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_sla_target_error_component import (
            ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_slo_target_error_component import (
            ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_sync_mode_error_component import (
            ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_target_availability_error_component import (
            ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_update_tolerations_error_component import (
            ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent
                | ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent
                | ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent
                | ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent
                | ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent
                | ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent
                | ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent
                | ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent
                | ApiV1IdpIdentityprovidersUpdateKindErrorComponent
                | ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent
                | ApiV1IdpIdentityprovidersUpdateNameErrorComponent
                | ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent
                | ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent
                | ApiV1IdpIdentityprovidersUpdateProviderErrorComponent
                | ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent
                | ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent
                | ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent
                | ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent
                | ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent
                | ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponent
                | ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_0 = (
                        ApiV1IdpIdentityprovidersUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_1 = (
                        ApiV1IdpIdentityprovidersUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_2 = (
                        ApiV1IdpIdentityprovidersUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_3 = (
                        ApiV1IdpIdentityprovidersUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_4 = (
                        ApiV1IdpIdentityprovidersUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_5 = (
                        ApiV1IdpIdentityprovidersUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_6 = (
                        ApiV1IdpIdentityprovidersUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_7 = (
                        ApiV1IdpIdentityprovidersUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_8 = (
                        ApiV1IdpIdentityprovidersUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_9 = (
                        ApiV1IdpIdentityprovidersUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_10 = (
                        ApiV1IdpIdentityprovidersUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_11 = (
                        ApiV1IdpIdentityprovidersUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_12 = (
                        ApiV1IdpIdentityprovidersUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_13 = (
                        ApiV1IdpIdentityprovidersUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_14 = (
                        ApiV1IdpIdentityprovidersUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_15 = (
                        ApiV1IdpIdentityprovidersUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_16 = (
                        ApiV1IdpIdentityprovidersUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_17 = (
                        ApiV1IdpIdentityprovidersUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_18 = (
                        ApiV1IdpIdentityprovidersUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_19 = (
                        ApiV1IdpIdentityprovidersUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_20 = (
                        ApiV1IdpIdentityprovidersUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_21 = (
                        ApiV1IdpIdentityprovidersUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_update_error_type_22 = (
                        ApiV1IdpIdentityprovidersUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_idp_identityproviders_update_error_type_23 = (
                    ApiV1IdpIdentityprovidersUpdateSyncModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_idp_identityproviders_update_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_idp_identityproviders_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_idp_identityproviders_update_validation_error.additional_properties = d
        return api_v1_idp_identityproviders_update_validation_error

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
