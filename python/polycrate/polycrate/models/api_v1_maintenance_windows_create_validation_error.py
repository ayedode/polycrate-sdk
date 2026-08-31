from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenance_windows_create_annotations_error_component import (
        ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_archived_at_error_component import (
        ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_archived_error_component import (
        ApiV1MaintenanceWindowsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_archived_reason_error_component import (
        ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_criticality_error_component import (
        ApiV1MaintenanceWindowsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_debug_mode_error_component import (
        ApiV1MaintenanceWindowsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_description_error_component import (
        ApiV1MaintenanceWindowsCreateDescriptionErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_display_name_error_component import (
        ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_is_system_default_error_component import (
        ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_kind_error_component import (
        ApiV1MaintenanceWindowsCreateKindErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_labels_error_component import (
        ApiV1MaintenanceWindowsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_lead_time_days_error_component import (
        ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_name_error_component import (
        ApiV1MaintenanceWindowsCreateNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_non_field_errors_error_component import (
        ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_note_error_component import (
        ApiV1MaintenanceWindowsCreateNoteErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_notice_required_error_component import (
        ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_platform_service_error_component import (
        ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_provider_error_component import (
        ApiV1MaintenanceWindowsCreateProviderErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_provider_id_error_component import (
        ApiV1MaintenanceWindowsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_provider_reference_error_component import (
        ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_reconciliation_enabled_error_component import (
        ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_sla_availability_error_component import (
        ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_sla_target_error_component import (
        ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_slo_availability_error_component import (
        ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_slo_target_error_component import (
        ApiV1MaintenanceWindowsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_target_availability_error_component import (
        ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_time_slots_error_component import (
        ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_create_tolerations_error_component import (
        ApiV1MaintenanceWindowsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenanceWindowsCreateValidationError")


@_attrs_define
class ApiV1MaintenanceWindowsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent |
            ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent | ApiV1MaintenanceWindowsCreateArchivedErrorComponent |
            ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent |
            ApiV1MaintenanceWindowsCreateCriticalityErrorComponent | ApiV1MaintenanceWindowsCreateDebugModeErrorComponent |
            ApiV1MaintenanceWindowsCreateDescriptionErrorComponent | ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent
            | ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent | ApiV1MaintenanceWindowsCreateKindErrorComponent |
            ApiV1MaintenanceWindowsCreateLabelsErrorComponent | ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent |
            ApiV1MaintenanceWindowsCreateNameErrorComponent | ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent |
            ApiV1MaintenanceWindowsCreateNoteErrorComponent | ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent |
            ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent | ApiV1MaintenanceWindowsCreateProviderErrorComponent
            | ApiV1MaintenanceWindowsCreateProviderIdErrorComponent |
            ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent |
            ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent |
            ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent |
            ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsCreateSloTargetErrorComponent |
            ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponent | ApiV1MaintenanceWindowsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent
        | ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent
        | ApiV1MaintenanceWindowsCreateArchivedErrorComponent
        | ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent
        | ApiV1MaintenanceWindowsCreateCriticalityErrorComponent
        | ApiV1MaintenanceWindowsCreateDebugModeErrorComponent
        | ApiV1MaintenanceWindowsCreateDescriptionErrorComponent
        | ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent
        | ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent
        | ApiV1MaintenanceWindowsCreateKindErrorComponent
        | ApiV1MaintenanceWindowsCreateLabelsErrorComponent
        | ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent
        | ApiV1MaintenanceWindowsCreateNameErrorComponent
        | ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent
        | ApiV1MaintenanceWindowsCreateNoteErrorComponent
        | ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent
        | ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent
        | ApiV1MaintenanceWindowsCreateProviderErrorComponent
        | ApiV1MaintenanceWindowsCreateProviderIdErrorComponent
        | ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent
        | ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent
        | ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent
        | ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsCreateSloTargetErrorComponent
        | ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponent
        | ApiV1MaintenanceWindowsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenance_windows_create_annotations_error_component import (
            ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_archived_at_error_component import (
            ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_archived_error_component import (
            ApiV1MaintenanceWindowsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_archived_reason_error_component import (
            ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_criticality_error_component import (
            ApiV1MaintenanceWindowsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_debug_mode_error_component import (
            ApiV1MaintenanceWindowsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_description_error_component import (
            ApiV1MaintenanceWindowsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_display_name_error_component import (
            ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_is_system_default_error_component import (
            ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_kind_error_component import (
            ApiV1MaintenanceWindowsCreateKindErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_labels_error_component import (
            ApiV1MaintenanceWindowsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_name_error_component import (
            ApiV1MaintenanceWindowsCreateNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_note_error_component import (
            ApiV1MaintenanceWindowsCreateNoteErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_notice_required_error_component import (
            ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_platform_service_error_component import (
            ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_provider_error_component import (
            ApiV1MaintenanceWindowsCreateProviderErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_provider_id_error_component import (
            ApiV1MaintenanceWindowsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_provider_reference_error_component import (
            ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_sla_availability_error_component import (
            ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_sla_target_error_component import (
            ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_slo_availability_error_component import (
            ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_slo_target_error_component import (
            ApiV1MaintenanceWindowsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_target_availability_error_component import (
            ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_tolerations_error_component import (
            ApiV1MaintenanceWindowsCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsCreateNoteErrorComponent):
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
        from ..models.api_v1_maintenance_windows_create_annotations_error_component import (
            ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_archived_at_error_component import (
            ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_archived_error_component import (
            ApiV1MaintenanceWindowsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_archived_reason_error_component import (
            ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_criticality_error_component import (
            ApiV1MaintenanceWindowsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_debug_mode_error_component import (
            ApiV1MaintenanceWindowsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_description_error_component import (
            ApiV1MaintenanceWindowsCreateDescriptionErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_display_name_error_component import (
            ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_is_system_default_error_component import (
            ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_kind_error_component import (
            ApiV1MaintenanceWindowsCreateKindErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_labels_error_component import (
            ApiV1MaintenanceWindowsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_name_error_component import (
            ApiV1MaintenanceWindowsCreateNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_note_error_component import (
            ApiV1MaintenanceWindowsCreateNoteErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_notice_required_error_component import (
            ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_platform_service_error_component import (
            ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_provider_error_component import (
            ApiV1MaintenanceWindowsCreateProviderErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_provider_id_error_component import (
            ApiV1MaintenanceWindowsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_provider_reference_error_component import (
            ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_sla_availability_error_component import (
            ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_sla_target_error_component import (
            ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_slo_availability_error_component import (
            ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_slo_target_error_component import (
            ApiV1MaintenanceWindowsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_target_availability_error_component import (
            ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_time_slots_error_component import (
            ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_create_tolerations_error_component import (
            ApiV1MaintenanceWindowsCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent
                | ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent
                | ApiV1MaintenanceWindowsCreateArchivedErrorComponent
                | ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent
                | ApiV1MaintenanceWindowsCreateCriticalityErrorComponent
                | ApiV1MaintenanceWindowsCreateDebugModeErrorComponent
                | ApiV1MaintenanceWindowsCreateDescriptionErrorComponent
                | ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent
                | ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent
                | ApiV1MaintenanceWindowsCreateKindErrorComponent
                | ApiV1MaintenanceWindowsCreateLabelsErrorComponent
                | ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent
                | ApiV1MaintenanceWindowsCreateNameErrorComponent
                | ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent
                | ApiV1MaintenanceWindowsCreateNoteErrorComponent
                | ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent
                | ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent
                | ApiV1MaintenanceWindowsCreateProviderErrorComponent
                | ApiV1MaintenanceWindowsCreateProviderIdErrorComponent
                | ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent
                | ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent
                | ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent
                | ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsCreateSloTargetErrorComponent
                | ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponent
                | ApiV1MaintenanceWindowsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_0 = (
                        ApiV1MaintenanceWindowsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_1 = (
                        ApiV1MaintenanceWindowsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_2 = (
                        ApiV1MaintenanceWindowsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_3 = (
                        ApiV1MaintenanceWindowsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_4 = (
                        ApiV1MaintenanceWindowsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_5 = (
                        ApiV1MaintenanceWindowsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_6 = (
                        ApiV1MaintenanceWindowsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_7 = (
                        ApiV1MaintenanceWindowsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_8 = (
                        ApiV1MaintenanceWindowsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_9 = (
                        ApiV1MaintenanceWindowsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_10 = (
                        ApiV1MaintenanceWindowsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_11 = (
                        ApiV1MaintenanceWindowsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_12 = (
                        ApiV1MaintenanceWindowsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_13 = (
                        ApiV1MaintenanceWindowsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_14 = (
                        ApiV1MaintenanceWindowsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_15 = (
                        ApiV1MaintenanceWindowsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_16 = (
                        ApiV1MaintenanceWindowsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_17 = (
                        ApiV1MaintenanceWindowsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_18 = (
                        ApiV1MaintenanceWindowsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_19 = (
                        ApiV1MaintenanceWindowsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_20 = (
                        ApiV1MaintenanceWindowsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_21 = (
                        ApiV1MaintenanceWindowsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_22 = (
                        ApiV1MaintenanceWindowsCreateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_23 = (
                        ApiV1MaintenanceWindowsCreateLeadTimeDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_24 = (
                        ApiV1MaintenanceWindowsCreateNoticeRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_25 = (
                        ApiV1MaintenanceWindowsCreateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_create_error_type_26 = (
                        ApiV1MaintenanceWindowsCreateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenance_windows_create_error_type_27 = (
                    ApiV1MaintenanceWindowsCreateTimeSlotsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenance_windows_create_error_type_27

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenance_windows_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenance_windows_create_validation_error.additional_properties = d
        return api_v1_maintenance_windows_create_validation_error

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
