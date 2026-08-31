from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_idp_identityproviders_partial_update_annotations_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_archived_at_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_archived_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_archived_reason_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_criticality_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_debug_mode_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_display_name_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_hostname_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_kind_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_labels_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_name_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_non_field_errors_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_platform_service_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_provider_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_provider_id_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_provider_reference_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_reconciliation_enabled_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_sla_availability_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_sla_target_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_slo_availability_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_slo_target_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_sync_mode_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_target_availability_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_idp_identityproviders_partial_update_tolerations_error_component import (
        ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IdpIdentityprovidersPartialUpdateValidationError")


@_attrs_define
class ApiV1IdpIdentityprovidersPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_idp_identityproviders_partial_update_annotations_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_archived_at_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_archived_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_criticality_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_display_name_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_hostname_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_kind_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_labels_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_name_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_platform_service_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_provider_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_provider_id_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_sla_target_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_slo_target_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_target_availability_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_tolerations_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent):
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
        from ..models.api_v1_idp_identityproviders_partial_update_annotations_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_archived_at_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_archived_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_archived_reason_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_criticality_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_debug_mode_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_display_name_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_hostname_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_kind_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_labels_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_name_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_non_field_errors_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_platform_service_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_provider_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_provider_id_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_provider_reference_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_reconciliation_enabled_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_sla_availability_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_sla_target_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_slo_availability_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_slo_target_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_sync_mode_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_target_availability_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_idp_identityproviders_partial_update_tolerations_error_component import (
            ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_0 = (
                        ApiV1IdpIdentityprovidersPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_1 = (
                        ApiV1IdpIdentityprovidersPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_2 = (
                        ApiV1IdpIdentityprovidersPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_3 = (
                        ApiV1IdpIdentityprovidersPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_4 = (
                        ApiV1IdpIdentityprovidersPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_5 = (
                        ApiV1IdpIdentityprovidersPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_6 = (
                        ApiV1IdpIdentityprovidersPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_7 = (
                        ApiV1IdpIdentityprovidersPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_8 = (
                        ApiV1IdpIdentityprovidersPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_9 = (
                        ApiV1IdpIdentityprovidersPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_10 = (
                        ApiV1IdpIdentityprovidersPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_11 = (
                        ApiV1IdpIdentityprovidersPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_12 = (
                        ApiV1IdpIdentityprovidersPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_13 = (
                        ApiV1IdpIdentityprovidersPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_14 = (
                        ApiV1IdpIdentityprovidersPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_15 = (
                        ApiV1IdpIdentityprovidersPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_16 = (
                        ApiV1IdpIdentityprovidersPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_17 = (
                        ApiV1IdpIdentityprovidersPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_18 = (
                        ApiV1IdpIdentityprovidersPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_19 = (
                        ApiV1IdpIdentityprovidersPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_20 = (
                        ApiV1IdpIdentityprovidersPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_21 = (
                        ApiV1IdpIdentityprovidersPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_22 = (
                        ApiV1IdpIdentityprovidersPartialUpdateHostnameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_23 = (
                    ApiV1IdpIdentityprovidersPartialUpdateSyncModeErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_idp_identityproviders_partial_update_error_type_23

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_idp_identityproviders_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_idp_identityproviders_partial_update_validation_error.additional_properties = d
        return api_v1_idp_identityproviders_partial_update_validation_error

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
